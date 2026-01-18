from datetime import datetime, date, time, timedelta
from dbSetup import engine
import pandas as pd
from services.dbServices import db
from sqlalchemy import text

class ProfsPlanner:
    def __init__(self,exams_df,exam_sessions_df,exam_supervisions_df,professors_df):
        self.max_per_day = 3
        self.ProfessorsSupervisionSchedule = {} 
        self.ProfessorsSupervisionAvailability = {}
        self.exams_df = exams_df
        self.exam_sessions_df = exam_sessions_df
        self.exam_supervisions_df = exam_supervisions_df
        self.professors_df = professors_df
        self.new_exam_profs_supervisions = pd.DataFrame(columns=[
            "exam_session_id",
            "professor_id"
        ])

    def loadDictionaryForDate(self,Date):
        self.ProfessorsSupervisionSchedule[Date] = self.loadProfessorsSupervisionScheduleForDate(Date)
        self.ProfessorsSupervisionAvailability[Date] = self.loadProfessorsSupervisionAvailabilityForDate(self.ProfessorsSupervisionSchedule[Date])

    def loadProfessorsSupervisionScheduleForDate(self, Date):
        df = (
            self.exam_supervisions_df
            .merge(self.exam_sessions_df, left_on='exam_session_id', right_on='id', suffixes=('', '_session'))
            .merge(self.exams_df, left_on='exam_id', right_on='id', suffixes=('', '_exam'))
        )

        df = df[df['exam_date'] == Date]

        df = df[['professor_id', 'exam_date', 'exam_time']].copy()
        df.rename(columns={'professor_id': 'prof_id'}, inplace=True)
        return df
    
    def loadProfessorsSupervisionAvailabilityForDate(self, ProfessorsSupervisionSchedule):
        supervision_counts = (
            ProfessorsSupervisionSchedule
            .groupby('prof_id')              
            .size()                      
            .reset_index(name='supervision_done')
        )

        df = self.professors_df[['id', 'department_id']].copy()
        df = df.merge(supervision_counts, how='left', left_on='id', right_on='prof_id')

        df['supervision_done'] = df['supervision_done'].fillna(0).astype(int)

        df['supervision_count'] = self.max_per_day - df['supervision_done']

        df = df[['id', 'supervision_count', 'department_id']].copy()
        df.rename(columns={'id': 'professor_id'}, inplace=True)

        df = df.sort_values(by=['department_id', 'supervision_count'], ascending=[False, False])
        return df

    def checkIsAvailableTime(self,Time):

        return True
    
    def saveExamProfsSupervisionsInDb(self):
        if self.new_exam_profs_supervisions.empty:
            # print("\nNo professor supervisions to save.")
            return

        try:
            query = text("""
                INSERT INTO exam_supervisions (exam_session_id, professor_id)
                VALUES (:exam_session_id, :professor_id)
            """)

            for _, row in self.new_exam_profs_supervisions.iterrows():
                db.execute(query, {
                    "exam_session_id": str(row["exam_session_id"]),
                    "professor_id": int(row["professor_id"])
                })

            db.commit()
            # print(f"\n{len(self.new_exam_profs_supervisions)} professor reservations saved successfully.")

        except Exception as e:
            db.rollback()
            # print("\nError saving professor reservations:", e)

        finally:
            db.close()


    def reserveProfs(self, examSessionId, Date, Time, num_profs=3): 
    
        # print(f"              Start prof reservation for exam session id : {examSessionId}")

        # 1️⃣ Load date if not exists
        if Date not in self.ProfessorsSupervisionSchedule or Date not in self.ProfessorsSupervisionAvailability:
            self.loadDictionaryForDate(Date)
        # print(f"\n\n{self.ProfessorsSupervisionAvailability}\n\n")
        # print(f"\n\n{self.ProfessorsSupervisionSchedule}\n\n")
        df_avail = self.ProfessorsSupervisionAvailability[Date]
        df_schedule = self.ProfessorsSupervisionSchedule[Date]
        # 2️⃣ Filter professors who still have slots AND are free at this exact Time
        available_profs = df_avail[
            (df_avail['supervision_count'] > 0) &
            (~df_avail['professor_id'].isin(
                df_schedule[df_schedule['exam_time'] == Time]['prof_id']
            ))
        ]
        # print("avalable profd are",available_profs)
        # 3️⃣ Pick the first `num_profs`
        selected = available_profs.head(num_profs)

        if selected.empty:
            # print("No available professors for this time!")
            return pd.DataFrame()  # or handle differently

        # 4️⃣ Update supervision_count and schedule
        new_rows = []
        for idx in selected.index:
            # Decrease remaining slots
            df_avail.at[idx, 'supervision_count'] -= 1

            # Prepare new schedule row
            new_rows.append({
                'prof_id': df_avail.at[idx, 'professor_id'],
                'exam_date': Date,
                'exam_time': Time
            })

            #save profs for the db Table
            # self.new_exam_profs_supervisions.append({
            #     'exam_session_id': examSessionId,
            #     'professor_id': df_avail.at[idx, 'professor_id']
            # })

            self.new_exam_profs_supervisions = pd.concat([
                self.new_exam_profs_supervisions,
                pd.DataFrame([{
                    "exam_session_id": examSessionId,
                    "professor_id": df_avail.at[idx, "professor_id"]
                }])
            ], ignore_index=True)


        # Append all new rows at once
        self.ProfessorsSupervisionSchedule[Date] = pd.concat(
            [df_schedule, pd.DataFrame(new_rows)],
            ignore_index=True
        )

        # 5️⃣ Re-sort availability: department_id=4 first, then remaining slots descending
        df_avail.sort_values(by=['department_id', 'supervision_count'], ascending=[False, False], inplace=True)

        # print("Updated availability:\n", df_avail)
        # print("Reserved professors:\n", selected[['professor_id', 'supervision_count']])
        
        # print(f"\n\n{self.ProfessorsSupervisionAvailability[Date]}\n\n")
        # print(f"\n\n{self.ProfessorsSupervisionAvailability[Date][self.ProfessorsSupervisionAvailability[Date]["department_id"]==7]}\n\n")
        # print(f"\n\n{self.ProfessorsSupervisionSchedule}\n\n")


        # print("              Reserved profs are: ", selected['professor_id'].to_list())
        # print("              Finish prof reservation")

        return