from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/admin")

@router.get("/dashboard")
def admin_dashboard(user=Depends(get_current_user)):
    
    if user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")

    return {"message": "admin API Running 🚀"}