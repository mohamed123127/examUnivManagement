from datetime import datetime, date, time, timedelta
import pandas as pd
from services.ClassroomsPlannerServices import ClassroomsPlanner
from services.ProfsPlannerService import ProfsPlanner
from collections import Counter
from helpers.printer import jsonPrint
from helpers.statistiquesCalculator import getStatistiques
import time as timer
from services.dbServices import db,get_next_auto_increment
from sqlalchemy import text

class ExamPlanner:
    def __init__(self, db):
        # Convert all tables to pandas DataFrames
        self.roles_df = pd.DataFrame(db["roles"])
        self.departments_df = pd.DataFrame(db["departments"])
        self.formations_df = pd.DataFrame(db["formations"])
        self.formation_years_df = pd.DataFrame(db["formation_years"])
        self.modules_df = pd.DataFrame(db["modules"])
        self.formation_year_modules_df = pd.DataFrame(db["formation_year_modules"])
        self.groups_df = pd.DataFrame(db["groups"])
        self.professors_df = pd.DataFrame(db["professors"])
        self.classrooms_df = pd.DataFrame(db["classrooms"])
        
        # init columns in exams
        self.exams_df = pd.DataFrame(db["exams"])
        if self.exams_df.empty:
            self.exams_df = pd.DataFrame(columns=["id", "module_id", "exam_date", "exam_time"])

        # init columns in exam_sessions
        self.exam_sessions_df = pd.DataFrame(db["exam_sessions"])
        if self.exam_sessions_df.empty:
            self.exam_sessions_df = pd.DataFrame(columns=["id", "exam_id", "classroom_id","group_id","part"])

        # init columns in exam_supervisions
        self.exam_supervisions_df = pd.DataFrame(db["exam_supervisions"])
        if self.exam_supervisions_df.empty:
            self.exam_supervisions_df = pd.DataFrame(columns=["id", "exam_session_id", "professor_id"])

        self.minumumModuleGroups = 0
        self.next_exam_Id = 0

        # Exam scheduling attributes
        self.examStartDay = date(2025, 12, 24)
        self.examEndDay = date(2026, 1, 24)
        self.minDaysBetweenExams = 1
        self.examsTimes = [time(8, 30), time(10, 15), time(12), time(13, 45), time(15, 30)]
        self.currentTimeIndex = 0
        self.currentDate = self.examStartDay
        self.newExams = pd.DataFrame(columns=["module_id", "exam_date", "exam_time"])
        self.dateTimeAvailabilities = {}
        self.unreservedModules = [] 
        self.currentFormationYear = 0
        self.TotalFormationYear = len(self.formation_years_df)

        # Planners
        self.profsPlanner = ProfsPlanner(self.exams_df,self.exam_sessions_df,self.exam_supervisions_df,self.professors_df)
        self.classroomsPlanner = ClassroomsPlanner(self.examsTimes,self.classrooms_df, self.exams_df, self.exam_sessions_df,self.formation_year_modules_df,self.groups_df,self.profsPlanner)
        
    def calcMinumumModuleGroups(self):
        counts = self.groups_df.groupby("formation_year_id").size()
        min_count = counts.min()
        return min_count

    def nextAvailableDay(self, currentDate, daysPlus=None):
        if daysPlus is not None:
            nextDate = currentDate + timedelta(days=daysPlus)
        else:
            nextDate = currentDate + timedelta(days=self.minDaysBetweenExams + 1)

        # Skip Friday
        if nextDate.weekday() == 4:
            nextDate += timedelta(days=1)

        return nextDate


    def nextAvailableTime(self):
        self.currentTimeIndex = (self.currentTimeIndex + 1) % len(self.examsTimes)
        return

    def isTimeAvailable(self, module_id, exam_date):
        dt = datetime.combine(exam_date, self.examsTimes[self.currentTimeIndex])
        return self.profsPlanner.isProfAvailable(dt) and self.classroomsPlanner.isClassroomsAvailable(dt)

    def getReservedExams(self, modulesIds):
        reserved = self.exams_df[self.exams_df["module_id"].astype(int).isin(modulesIds)]
        return reserved

    def loadDateTimeAvailabilities(self, Date):
        """
        For each exam time, compute how many groups can pass exams
        based on classrooms + professors availability
        """

        self.dateTimeAvailabilities.setdefault(Date, {})

        # Load classrooms availability for this date
        if Date not in self.classroomsPlanner.availableClassrooms:
            self.classroomsPlanner.loadClassroomsForDate(Date)
        # Load professors availability & schedule for this date
        if Date not in self.profsPlanner.ProfessorsSupervisionSchedule or Date not in self.profsPlanner.ProfessorsSupervisionAvailability:
            self.profsPlanner.loadDictionaryForDate(Date)

        df_day_avail = self.profsPlanner.ProfessorsSupervisionAvailability[Date]
        df_day_schedule = self.profsPlanner.ProfessorsSupervisionSchedule[Date]

        for exam_time in self.examsTimes:
            df_rooms = self.classroomsPlanner.availableClassrooms[Date][exam_time]

            amphis = df_rooms[(df_rooms['isAvailable']) & (df_rooms['type'] == 'amphi')]
            classes = df_rooms[(df_rooms['isAvailable']) & (df_rooms['type'] == 'class')]

            num_amphis = len(amphis)
            num_class_pairs = len(classes) // 2

            busy_profs = df_day_schedule[
                df_day_schedule['exam_time'] == exam_time
            ]['prof_id']

            available_profs = df_day_avail[
                (df_day_avail['supervision_count'] > 0) &
                (~df_day_avail['professor_id'].isin(busy_profs))
            ]

            num_available_profs = len(available_profs)

            max_groups_by_profs = 0

            # Use amphis first (3 profs)
            usable_amphis = min(num_amphis, num_available_profs // 3)
            max_groups_by_profs += usable_amphis
            num_available_profs -= usable_amphis * 3

            # Then class pairs (4 profs)
            usable_class_groups = min(num_class_pairs, num_available_profs // 4)
            max_groups_by_profs += usable_class_groups
            num_available_profs -= usable_class_groups * 4

            self.dateTimeAvailabilities[Date][exam_time] = max_groups_by_profs

        return self.dateTimeAvailabilities[Date]

    def getGroupsNumberForModule(self,module_id):
        formationsYearsWillPassThisExam = self.formation_year_modules_df[self.formation_year_modules_df['module_id']==module_id]['formation_year_id']
        groupsNumber = len(self.groups_df[self.groups_df['formation_year_id'].isin(formationsYearsWillPassThisExam)])
        return groupsNumber
    
    def checkIsAvailableTime(self,Date,groupNeeded,Time=None):
        #returned False if is not time available for this date
        #else reruned the time
        availableTimes = [T for T, capacity in self.dateTimeAvailabilities[Date].items() if capacity >= groupNeeded]
        if len(availableTimes) > 0:
            availableTime = availableTimes[0]
            if Time is not None and Time in availableTimes: return Time
            return availableTime
        return False

    def getNextExamId(self):
        self.next_exam_Id = self.next_exam_Id + 1
        return self.next_exam_Id

    def checkIsAvailableDateTime(self, Date, Time, reservedExams, groupsNeeded):
        ###return false if No available time for groupsNeeded
        ###else return the Date and Time

        while Date <= self.examEndDay:
            # تحقق من التعارض مع الامتحانات السابقة
            min_date = Date - timedelta(days=self.minDaysBetweenExams)
            max_date = Date + timedelta(days=self.minDaysBetweenExams)

            conflictInDate = reservedExams[
                (reservedExams['exam_date'] >= min_date) &
                (reservedExams['exam_date'] <= max_date)
            ]

            if conflictInDate.empty:
                # if no conflit then check is available time
                self.loadDateTimeAvailabilities(Date)
                availableTime = self.checkIsAvailableTime(Date, groupsNeeded, Time)
                if availableTime:
                    #return date and time available
                    return Date, availableTime
                #next day
                Date += timedelta(days=1)
            else:
                #we have conflite , let's select how much day we need after the conflit day
                nearest_conflict_date = conflictInDate['exam_date'].min()
                daysPlus = (nearest_conflict_date - Date).days + self.minDaysBetweenExams + 1
                Date = self.nextAvailableDay(Date, daysPlus)

        #if we pass last exam date
        print(f"❌ Exams period ended. No available time for {groupsNeeded} groups.")
        return False

    def saveExamsInDb(self):
        if self.newExams.empty:
            print("\nNo new exams to save.")
            return
        try:
            query = text("""
                INSERT INTO exams (id,module_id, exam_date, exam_time)
                VALUES (:id,:module_id, :exam_date, :exam_time)
            """)
            for _, exam in self.newExams.iterrows():
                db.execute(query, {
                    "id": int(exam["id"]),
                    "module_id": int(exam["module_id"]),
                    "exam_date": exam["exam_date"],
                    "exam_time": exam["exam_time"]
                })
            db.commit()
            # print(f"\n{len(self.newExams)} exams saved successfully.")
        except Exception as e:
            db.rollback()
            print("\nError saving exams:", e)
        finally:
            db.close()

    def saveReservationsInDb(self):
        self.saveExamsInDb()
        self.classroomsPlanner.saveExamSessionsInDb()
        self.profsPlanner.saveExamProfsSupervisionsInDb()
        return

    def formationYearReservation(self, formationYearId):
        # print("start reservation for formation year id : ",formationYearId)
        self.currentFormationYear = self.currentFormationYear +1

        # Get all modules for this formation year
        modulesIds = self.formation_year_modules_df[
            self.formation_year_modules_df["formation_year_id"] == formationYearId
        ]["module_id"].tolist()

        # Check reserved modules
        reservedExams = self.getReservedExams(modulesIds)
        reservedIds = reservedExams["module_id"].astype(int).tolist()

        # Remove already reserved module IDs from modulesIds
        modulesIds = [m for m in modulesIds if m not in reservedIds]
        nextModuleExamDate = self.currentDate

        # print("Modules for reservation for this year are: ",modulesIds)
        for module_id in modulesIds:
            # print("\n    start reservation for module id : ",module_id)
            #check the Date and time is it available
            groupsNeeded= self.getGroupsNumberForModule(module_id)
            result = self.checkIsAvailableDateTime(nextModuleExamDate,self.examsTimes[0],reservedExams,groupsNeeded)
            if(result is False): 
                self.unreservedModules.append({
                    "module_id": module_id,
                    "groupsNeeded": groupsNeeded,
                    "problem": "dosnt find any date time have enough resources for this module"
                })
                continue
            else:
                nextModuleExamDate, nextModuleExamTime = result

            nextExamId = self.getNextExamId()

            new_exam = pd.DataFrame([{
                "id": nextExamId,
                "module_id": module_id,
                "exam_date": nextModuleExamDate,
                "exam_time": nextModuleExamTime
            }])

            self.newExams = pd.concat([self.newExams, new_exam], ignore_index=True)
            # print(
            #     "    the exams was programmed at:",
            #     new_exam["exam_date"].iloc[0],
            #     new_exam["exam_time"].iloc[0]
            # )
            # print(f"\n\n{self.next_exam_Id}\n\n")

            self.classroomsPlanner.reserveClassrooms(self.next_exam_Id,module_id,nextModuleExamDate,nextModuleExamTime)
            # print("    finish reservation for module id : ",module_id)
            # Move to next day
            nextModuleExamDate = self.nextAvailableDay(nextModuleExamDate)
        
        # print("finish reservation for formation year id : ",formationYearId)

    def startPlanification(self):
        self.next_exam_Id = get_next_auto_increment("exams")
        #set a time
        start_time = timer.time()

        for i in range(len(self.formation_years_df)):
            self.formationYearReservation(i)
            
        self.saveReservationsInDb()
        print("\n\nissues:")
        jsonPrint(self.unreservedModules)

        end_time = timer.time()    # end timer
        elapsed_time = end_time - start_time
        print(f"Algorithms took {elapsed_time:.4f} seconds")
        return

