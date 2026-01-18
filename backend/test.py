from sqlalchemy import create_engine
import pandas as pd
import json
from datetime import date, time, datetime

# ---------- Database connection ----------
DATABASE_URL = "mysql+pymysql://root:@localhost/university_exam_planning_db"
engine = create_engine(DATABASE_URL)

# ---------- Tables you want to fetch ----------
tables = [
    "roles",
    "departments",
    "formations",
    "formation_years",
    "modules",
    "formation_year_modules",
    "groups",
    "professors",
    "classrooms",
    "exams",
    "exam_sessions",
    "exam_supervisions"
]

fake_db = {}

with engine.connect() as conn:
    for table in tables:
        df = pd.read_sql_table(table, conn)
        
        # Convert date/time columns correctly
        for col in df.columns:
            if "date" in col.lower():
                df[col] = pd.to_datetime(df[col]).dt.date
            elif "time" in col.lower():
                # Handle existing datetime.time or string properly
                df[col] = df[col].apply(lambda x: x if isinstance(x, time) else pd.to_datetime(x).time())
        
        fake_db[table] = df.to_dict(orient="records")

# ---------- Write to Python file ----------
with open("fake_db_from_sql.py", "w", encoding="utf-8") as f:
    f.write("# Auto-generated mock DB from MySQL\n\n")
    f.write("from datetime import date, time\n\n")
    f.write("fake_db = ")
    json_str = json.dumps(fake_db, default=str, indent=4)
    f.write(json_str)

print("✅ fake_db_from_sql.py generated successfully!")
