from fastapi import FastAPI
import uvicorn
from controller.DatabaseC import DatabaseController
from controller.TownsC import TownsController
from controller.FusilladesC import FusilladesController
from controller.NationalitiesC import NationalitiesController

from model.NationalitiesM import NationalityModel
from model.TownsM import TownModel
from model.FusilladesM import FusilladeModel
from controller.InvestigationsC import InvestigationsController
app = FastAPI()


@app.get("/create_database")
async def createDatabase():
    return DatabaseController.createDatabase()


################# Towns #############################################
@app.get("/towns")
async def getTowns():
    return TownsController.findAll()

@app.get("/town/{id}")
async def getTown(id):
    return TownsController.findById(id)

@app.post("/town")
async def createTown(town : TownModel):
    return TownsController.insertOne(town)


@app.put("/town")
async def updateTown(town : TownModel):
    return TownsController.update(town)

@app.delete("/town")
async def deleteTown(town : TownModel):
    return TownsController.delete(town.id)



################# Fusillades #############################################

@app.get("/fusillades")
async def getFusillades():
    return FusilladesController.findAll()

@app.get("/fusillade/{id}")
async def getFusillade(id):
    return FusilladesController.findById(id)

@app.post("/fusillade")
async def createFusillade(fusillade : FusilladeModel):
    return FusilladesController.insertOne(fusillade)

@app.put("/fusillade")
async def updateFusillade(fusillade : FusilladeModel):
    return FusilladesController.update(fusillade)

@app.delete("/fusillade")
async def deleteFusillade(fusillade : FusilladeModel):
    return FusilladesController.delete(fusillade.id)

@app.post("/solve_investigation") # pourquoi pas un get ? 
async def solveInvestigation(id):
    return InvestigationsController.solveInvestigation(id)


################# Nationalities #############################################

@app.get("/nationalities", tags=['Nationalities'], description="Operations sur la table Nationalities")
async def getNationalities():
    return NationalitiesController.findAll()

@app.get("/nationality/{id}", tags=['Nationalities'], description="Operations sur la table Nationalities")
async def getNationality(id):
    return NationalitiesController.findById(id)

@app.post("/nationality", tags=['Nationalities'], description="Operations sur la table Nationalities")
async def createNationality(nationality : NationalityModel):
    return NationalitiesController.insertOne(nationality)

@app.put("/nationality/{id}", tags=['Nationalities'], description="Operations sur la table Nationalities")
async def updateNationality(id : int,nationality : NationalityModel):
    print(id,nationality)
    return NationalitiesController.update(id,nationality)

@app.delete("/nationality/{id}", tags=['Nationalities'], description="Operations sur la table Nationalities")
async def deleteNationality(id : int):
    return NationalitiesController.delete(id)

if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)