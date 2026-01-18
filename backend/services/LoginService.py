from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session,joinedload
from dbSetup import SessionLocal
from models.user import User
from models.student import Student
from models.professor import Professor
from models.administration import Administration



def login(matricule: str, password: str, db: Session):
    print(matricule,"  ",password)
    user = (
        db.query(User)
        .options(joinedload(User.role))
        .filter(
            User.matricule == matricule,
            User.password == password
        )
        .first()
    )

    if not user:
        raise HTTPException(status_code=401, detail="Email or mot passe are wrong")

    base_user = {
        "id": user.id,
        "matricule": user.matricule,
        "role": user.role.name
    }

    # STUDENT
    if user.role_id == 1:
        student = db.query(Student).filter(
            Student.matricule == user.matricule
        ).first()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        base_user["id"] = student.id
        base_user["username"] = student.last_name + " " + student.first_name
        base_user["group_id"] = student.group_id
        base_user["group"] = student.group.group_number


    # PROFESSOR
    elif user.role_id == 2:
        prof = db.query(Professor).filter(
            Professor.matricule == user.matricule
        ).first()

        if not prof:
            raise HTTPException(status_code=404, detail="Professor not found")
        
        base_user["id"] = prof.id
        base_user["username"] = prof.last_name + " " + prof.first_name

    # ADMINISTRATION
    else:
        admin = db.query(Administration).filter(
            Administration.matricule == user.matricule
        ).first()

        if not admin:
            raise HTTPException(status_code=404, detail="Administration not found")

        base_user["id"] = admin.id
        base_user["username"] = admin.last_name + " " + admin.first_name
        base_user["dept_id"] = admin.department_id

    return {
        "message": "Login successful",
        "user": base_user
    }