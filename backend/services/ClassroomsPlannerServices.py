import pandas as pd
from datetime import datetime, date, time
from services.ProfsPlannerService import ProfsPlanner
from services.dbServices import db
from sqlalchemy import text


class ClassroomsPlanner:
    def __init__(self,examsTimes,classrooms_df, exams_df, exam_sessions_df,formation_year_modules_df,groups_df,profsPlanner:ProfsPlanner):
        self.examsTimes = examsTimes
        self.classrooms_df = classrooms_df
        self.exams_df = exams_df
        self.exam_sessions_df = exam_sessions_df
        self.formation_year_modules_df = formation_year_modules_df
        self.groups_df = groups_df
        self.profsPlanner = profsPlanner

        self.availableClassrooms = {}
        self.new_exam_sessions = pd.DataFrame(columns=["id", "exam_id", "classroom_id", "group_id", "part"])

    def loadClassroomsForDate(self, Date):
        exams_day_df = self.exams_df[self.exams_df['exam_date'] == Date]

        reserved_df = (
            self.exam_sessions_df
            .merge(
                exams_day_df,
                left_on='exam_id',
                right_on='id',
                suffixes=('', '_exam')
            )
        )

        reserved_df = reserved_df[['classroom_id', 'exam_time']]

        self.availableClassrooms[Date] = {}

        for exam_time in self.examsTimes:

            reserved_ids = set(
                reserved_df[reserved_df['exam_time'] == exam_time]['classroom_id']
            )

            df = self.classrooms_df[['id', 'type', 'capacity']].copy()
            df.rename(columns={'id': 'classroom_id'}, inplace=True)

            df['isAvailable'] = ~df['classroom_id'].isin(reserved_ids)
            df = df.sort_values(
                by=['isAvailable', 'capacity'],
                ascending=[False, False]
            ).reset_index(drop=True)
            self.availableClassrooms[Date][exam_time] = df
        

        return self.availableClassrooms[Date]

    def isClassroomsAvailable(self, dt: datetime):
        dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        if dt_str in self.availableClasses:
            return self.availableClasses[dt_str] > 0
        return True
    
    def getGroupsFromModuleId(self,module_id):
        formationYearsIds = self.formation_year_modules_df[self.formation_year_modules_df['module_id']==module_id]['formation_year_id']
        groupsIds = self.groups_df[self.groups_df['formation_year_id'].isin(formationYearsIds)]['id']
        return groupsIds

    def saveExamSessionsInDb(self):
        if self.new_exam_sessions.empty:
            print("\nNo new exam sessions to save.")
            return

        try:
            query = text("""
                INSERT INTO exam_sessions (id, exam_id, classroom_id, group_id, part)
                VALUES (:id, :exam_id, :classroom_id, :group_id, :part)
            """)

            # save classrooms in Db
            for _, session in self.new_exam_sessions.iterrows():

                db.execute(query, {
                    "id": str(session["id"]),
                    "exam_id": int(session["exam_id"]),
                    "classroom_id": int(session["classroom_id"]),
                    "group_id": int(session["group_id"]),
                    "part": None if pd.isna(session["part"]) else session["part"]
                })

            db.commit()
            # print(f"\n{len(self.new_exam_sessions)} exam sessions saved successfully.")

        except Exception as e:
            db.rollback()
            print("\nError saving exam sessions details:", e)

        finally:
            db.close()


    def reserveClassrooms(self,exam_id, module_id, Date, Time):
        # print("         Start classrooms reservation...")
        #Load dictinary
        if Date not in self.availableClassrooms:
            self.loadClassroomsForDate(Date)
        df = self.availableClassrooms[Date][Time]

        # Get groups concerned by the module
        groupsIds = list(self.getGroupsFromModuleId(module_id))
        #reserved modules classrooms
        already_reserved_groups = self.exam_sessions_df[
            (self.exam_sessions_df['exam_id'] == exam_id) 
        ]['group_id'].unique()
        groupsIds = [g for g in groupsIds if g not in already_reserved_groups]
        # print(f"         Groups to assign: {groupsIds}")


        reservations = []
        # Loop over groups
        for group_id in groupsIds:
            # print(f"!! {group_id} !!")
            # Take first available classroom
            available = df[df['isAvailable'] == True]

            if available.empty:
                raise Exception("❌ Not enough classrooms available")

            classroom = available.iloc[0]
            classroom_id = classroom['classroom_id']
            classroom_type = classroom['type']

            if classroom_type == "amphi":
                # Save reservation row
                session_id = str(exam_id) + "_" + str(group_id)
                reservations.append({
                    "id": session_id,
                    "exam_id": exam_id,
                    "classroom_id": classroom_id,
                    "group_id": group_id,
                    "part": None
                })

                # Mark classroom as unavailable
                df.loc[df['classroom_id'] == classroom_id, 'isAvailable'] = False
                # print("         reserved class for group ",group_id," is Amphi id ",classroom_id)
                self.profsPlanner.reserveProfs(session_id,Date,Time,3)
            elif classroom_type == "class":
                # Need TWO classrooms
                if len(available) < 2:
                    raise Exception("❌ Not enough classrooms for class split")

                classA = available.iloc[0]
                classB = available.iloc[1]

                session_idA = str(exam_id) + "_" + str(group_id) + "_A"
                session_idB = str(exam_id) + "_" + str(group_id) + "_B"
                # Reserve part A
                reservations.append({
                    "id": session_idA,
                    "exam_id": exam_id,
                    "classroom_id": classA['classroom_id'],
                    "group_id": group_id,
                    "part": "A"
                })

                # Reserve part B
                reservations.append({
                    "id": session_idB,
                    "exam_id": exam_id,
                    "classroom_id": classB['classroom_id'],
                    "group_id": group_id,
                    "part": "B"
                })

                # print("         reserved class for group ",group_id," Part A is class id :",classA['classroom_id'])
                self.profsPlanner.reserveProfs(session_idA,Date,Time,2)
                # print("         reserved class for group ",group_id," Part B is class id :",classB['classroom_id'])
                self.profsPlanner.reserveProfs(session_idB,Date,Time,2)


                # Mark both as unavailable
                df.loc[df['classroom_id'] == classA['classroom_id'], 'isAvailable'] = False
                df.loc[df['classroom_id'] == classB['classroom_id'], 'isAvailable'] = False

            # Reorder dataframe (True first again)
            df.sort_values(
                by=['isAvailable', 'capacity'],
                ascending=[False, False],
                inplace=True
            )
            df.reset_index(drop=True, inplace=True)

        # Save back updated dataframe
        self.availableClassrooms[Date][Time] = df
        new_sessions_df = pd.DataFrame(reservations)

        self.new_exam_sessions = pd.concat(
            [self.new_exam_sessions, new_sessions_df],
            ignore_index=True
        )
        # print("         finish classrooms reservation")
        return 

