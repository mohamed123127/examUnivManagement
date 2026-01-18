from services.dbServices import load_db_to_memory,get_next_auto_increment
from services.ExamPlannerService import ExamPlanner
from helpers.statistiquesCalculator import getStatistiques

fake_db = load_db_to_memory()
planner = ExamPlanner(fake_db)
planner.startPlanification()
print("\n")
getStatistiques(fake_db)


