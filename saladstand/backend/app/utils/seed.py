from app.db.database import SessionLocal
from app.models.role import Role

def seed_roles():
    db = SessionLocal()

    roles = ["ADMIN", "CUSTOMER", "DELIVERY"]

    for r in roles:
        exists = db.query(Role).filter(Role.name == r).first()
        if not exists:
            db.add(Role(name=r))

    db.commit()
    db.close()