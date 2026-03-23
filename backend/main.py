from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SaladStand API is running"}