from fastapi import FastAPI
import uvicorn
from controller.DatabaseC import DatabaseController
from controller.TownsC import TownsController
from model.TownsM import TownModel
app = FastAPI()


@app.get("/create_database")
async def createDatabase():
    return "hey"
    res = DatabaseController.createDatabase()
    return res


@app.get("/towns")
async def getTowns():
    res = TownsController.findAll()
    return res

@app.post("/town")
async def createTown(town : TownModel):
    res = TownsController.insertOne(town)
    return res


if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=5001)