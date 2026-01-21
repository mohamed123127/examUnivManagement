from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, date, time
from models.base import Base
from models.department import Department
from dbSetup import get_db
from services.LoginService import login
from services import StudentService,ProfService,DataProviderService
from services.StatistiquesServices import StatsService
from models.module import Module
from models.formation_year import FormationYear
from models.formation import Formation
from models.department import Department
from sqlalchemy import distinct
from fastapi import Query
from services.dbServices import load_db_to_memory
from services.ExamPlannerService import ExamPlanner
from helpers.statistiquesCalculator import getStatistiques
from services.NotificationService import create_notification,get_all_notifications
from services.NotificationCreate import NotificationCreate
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware

app = FastAPI()
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")
fake_db = load_db_to_memory()
planner: ExamPlanner = ExamPlanner(fake_db)

origins = [
    "http://localhost:3000",  # frontend
    "http://127.0.0.1:3000",
    "https://exam-univ-management-r94ca0msg-louahchi-mohameds-projects.vercel.app",
    "https://exam-univ-management-git-main-louahchi-mohameds-projects.vercel.app",
    "http://exam-univ-management-git-main-louahchi-mohameds-projects.vercel.app",
    "http://exam-univ-management-r94ca0msg-louahchi-mohameds-projects.vercel.app",
    "https://examunivmanagement.vercel.app"
]

#solve issue of CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return "hello"

@app.get("/Modules")
def get_modules(db: Session = Depends(get_db)):
    rows = db.query(Module.id, Module.name).order_by(Module.name.asc()).all()
    return [{"id": r.id, "name": r.name} for r in rows]


# Departments
@app.get("/Departments")
def get_departments(db: Session = Depends(get_db)):
    rows = db.query(Department.id, Department.name).order_by(Department.name.asc()).all()
    return [{"id": r.id, "name": r.name} for r in rows]


# Formations
@app.get("/Formations")
def get_formations(db: Session = Depends(get_db)):
    rows = db.query(Formation.id, Formation.name).order_by(Formation.name.asc()).all()
    return [{"id": r.id, "name": r.name} for r in rows]


# Formation Years
@app.get("/FormationYears")
def get_formation_years(db: Session = Depends(get_db)):
    rows = db.query(distinct(FormationYear.year).label("name")).order_by(FormationYear.year.asc()).all()
    return [r.name for r in rows]


class LoginRequest(BaseModel):
    matricule: str
    password: str

@app.post("/login/")
def login_endpoint(data: LoginRequest, db: Session = Depends(get_db)):
    return login(matricule=data.matricule, password=data.password, db=db)

@app.get("/students/{group_id}/ExamsSchedule/")
def exams_endpoint(group_id, db: Session = Depends(get_db)):
    return StudentService.getExamsSchedule(group_id,db)

@app.get("/profs/{prof_id}/ExamsSchedule/")
def exams_endpoint(prof_id, db: Session = Depends(get_db)):
    return ProfService.getExamsSchedule(prof_id,db)

@app.get("/FormationYear/{page}")
def formationYear_endpoint(page:int,department_id: int | None = Query(None),formation_id: int | None = Query(None),year: str | None = Query(None),db: Session = Depends(get_db)):
    return DataProviderService.getAllFormationYearsData(db,page=page,department_id=department_id,year=year,formation_id=formation_id)

@app.get("/FormationYear/{formation_year_id}/Modules")
def formation_year_modules_endpoint(formation_year_id: int,db: Session = Depends(get_db)):
    return DataProviderService.getModulesByFormationYear(db, formation_year_id)

@app.get("/FormationYear/{formation_year_id}/Exams")
def formation_year_modules_endpoint(formation_year_id: int,db: Session = Depends(get_db)):
    return DataProviderService.getExamsByFormationYear(db, formation_year_id)

@app.get("/Classrooms")
def formation_year_modules_endpoint(Date: date,Time:str,db: Session = Depends(get_db)):
    return DataProviderService.getAvailableClassrooms(db,Date,Time)

@app.get("/StartPlanification")
def StartPlanification_endpoint():
    global planner 
    fake_db = load_db_to_memory()
    planner = ExamPlanner(fake_db)
    planner.startPlanification()
    print("\n")
    getStatistiques(fake_db)
    return {"status":"exams created successfuly"}

@app.get("/general-stats")
def general_stats_endpoint(db: Session = Depends(get_db),department_id: int | None = Query(None)):
    return StatsService.get_general_stats(db,department_id=department_id)


@app.get("/student-groups-stats")
def student_groups_stats_endpoint(db: Session = Depends(get_db),department_id: int | None = Query(None)):
    return StatsService.get_student_groups_stats(db,department_id=department_id)

@app.get("/exams-stats")
def exams_stats_endpoint(db: Session = Depends(get_db),department_id: int | None = Query(None)):
    return StatsService.get_exams_stats(db,department_id=department_id)
#
@app.get("/most-used-hours")
def most_used_hours_endpoint(db: Session = Depends(get_db),department_id: int | None = Query(None)):
    return StatsService.get_most_used_hours(db,department_id=department_id)


@app.get("/exam-per-department")
def exam_per_department_endpoint(db: Session = Depends(get_db),department_id: int | None = Query(None)):
    return StatsService.get_exam_per_department(db,department_id=department_id)

@app.post("/notification")
def add_notification(
    payload: NotificationCreate,
    db: Session = Depends(get_db)
):
    return create_notification(
        message=payload.message,
        type=payload.type,
        db=db
    )


@app.get("/notification")
def fetch_notifications(db: Session = Depends(get_db)):
    return get_all_notifications(db)

@app.get("/PlanificationProgress")
def get_progress():
    if planner.TotalFormationYear == 0:
        return {"progress": 0}
    return {"progress": (planner.currentFormationYear / planner.TotalFormationYear) * 100}
