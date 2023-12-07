from fastapi import FastAPI
from controller.DatabaseC import DatabaseController

app = FastAPI()

@app.get("/create_database")
async def createDatabase():
    return "hey"
    res = DatabaseController.createDatabase()
    return res