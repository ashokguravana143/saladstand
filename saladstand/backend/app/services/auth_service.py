from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, user_data):
    role = db.query(Role).filter(Role.name == "CUSTOMER").first()

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
        role_id=role.id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db: Session, user_data):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user or not verify_password(user_data.password, user.password):
        return None

    token = create_access_token({
        "user_id": user.id,
        "role": user.role.name
    })

    return token