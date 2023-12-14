from fastapi import FastAPI
import uvicorn
from controller.DatabaseC import DatabaseController
from controller.TownsC import TownsController
from controller.NationalitiesC import NationalitiesController
from controller.FusilladesC import FusilladesController
from controller.PersonsC import PersonsController
from controller.PolicemenC import PolicemenController
from controller.SuspectsC import SuspectsController
from model.TownsM import TownModel
from model.NationalitiesM import NationalityModel
from model.FusilladesM import FusilladeModel
from model.PersonsM import PersonModel
from model.PolicemenM import PolicemanModel
from model.SuspectsM import SuspectModel

app = FastAPI()

@app.get("/", tags=['Init'])
async def start():
    return {"Init msg": "Welcome to Dallas !"}

################# BDD #############################################

@app.get("/create_database", tags=['BDD'])
async def createDatabase():
    return DatabaseController.createDatabase()


################# Nationalities #############################################

@app.get("/Nationalities", tags=['Affichage'], description="Operations d'affichage")
async def getNationalities():
    return NationalitiesController.findAll()

@app.get("/Nationalities/{id}", tags=['Affichage'], description="Operations d'affichage")
async def getNationality(id):
    return NationalitiesController.findById(id)

@app.post("/Nationalities", tags=['Insertions'], description="Operations d'insertion")
async def createNationality(nationality : NationalityModel):
    return NationalitiesController.insertOne(nationality)

@app.put("/Nationalities", tags=['MaJ'], description="Mises à jour")
async def updateNationality(nationality : NationalityModel):
    return NationalitiesController.update(nationality)

@app.delete("/Nationalities", tags=['Suppression'], description="Operations de suppression")
async def deleteNationality(nationality : NationalityModel):
    return NationalitiesController.delete(nationality.id)


################# Towns #############################################

@app.get("/towns", tags=['Affichage'], description="Operations d'affichage")
async def getTowns():
    return TownsController.findAll()

@app.get("/town/{id}", tags=['Affichage'], description="Operations d'affichage")
async def getTown(id):
    return TownsController.findById(id)

@app.post("/town", tags=['Insertions'], description="Operations d'insertion")
async def createTown(town : TownModel):
    return TownsController.insertOne(town)

@app.put("/town", tags=['MaJ'], description="Mises à jour")
async def updateTown(town : TownModel):
    return TownsController.update(town)

@app.delete("/town", tags=['Suppression'], description="Operations de suppression")
async def deleteTown(town : TownModel):
    return TownsController.delete(town.id)


################# Fusillades #############################################

@app.get("/fusillades", tags=['Affichage'], description="Operations d'affichage")
async def getFusillades():
    return FusilladesController.findAll()

@app.get("/fusillade/{id}", tags=['Affichage'], description="Operations d'affichage")
async def getFusillade(id):
    return FusilladesController.findById(id)

@app.post("/fusillade", tags=['Insertions'], description="Operations d'insertion")
async def createFusillade(fusillade : FusilladeModel):
    return FusilladesController.insertOne(fusillade)

@app.put("/fusillade", tags=['MaJ'], description="Mises à jour")
async def updateFusillade(fusillade : FusilladeModel):
    return FusilladesController.update(fusillade)

@app.delete("/fusillade", tags=['Suppression'], description="Operations de suppression")
async def deleteFusillade(fusillade : FusilladeModel):
    return FusilladesController.delete(fusillade.id)


################## Persons ################################
@app.get("/persons", tags=['Affichage'], description="Operations d'affichage")
async def getPersons():
    return PersonsController.findAll()

@app.get("/persons/{id}", tags=['Affichage'], description="Operations d'affichage")
async def getPerson(id: int):
    return PersonsController.findById(id)

@app.post("/persons", tags=['Insertions'], description="Operations d'insertion")
async def createPerson(person : PersonModel):
    return PersonsController.insertOne(person)

@app.put("/persons", tags=['MaJ'], description="Mises à jour")
async def updatePerson(person : PersonModel):
    return PersonsController.update(person)

@app.delete("/persons", tags=['Suppression'], description="Operations de suppression")
async def deletePerson(person : PersonModel):
    return PersonsController.delete(person.id)


################## Policemen ################################
@app.get("/policemen", tags=['Affichage'], description="Operations d'affichage")
async def getPolicemen():
    return PolicemenController.findAll()

@app.get("/policemen/{id}", tags=['Affichage'], description="Operations d'affichage")
async def getPoliceman(id):
    return PolicemenController.findById(id)

@app.post("/policemen", tags=['Insertions'], description="Operations d'insertion")
async def createPoliceman(policeman : PolicemanModel):
    return PolicemenController.insertOne(policeman)

@app.put("/policemen", tags=['MaJ'], description="Mises à jour")
async def updatePoliceman(policeman : PolicemanModel):
    return PolicemenController.update(policeman)

@app.delete("/policemen", tags=['Suppression'], description="Operations de suppression")
async def deletePoliceman(policeman : PolicemanModel):
    return PolicemenController.delete(policeman.id)

################## Suspects ################################
@app.get("/suspects", tags=['Affichage'], description="Operations d'affichage")
async def getSuspects():
    return SuspectsController.findAll()

@app.get("/suspects/{id}", tags=['Affichage'], description="Operations d'affichage")
async def getSuspect(id):
    return SuspectsController.findById(id)

@app.post("/suspects", tags=['Insertions'], description="Operations d'insertion")
async def createSuspect(suspect : SuspectModel):
    return SuspectsController.insertOne(suspect)

@app.put("/suspects", tags=['MaJ'], description="Mises à jour")
async def updateSuspect(suspect : SuspectModel):
    return SuspectsController.update(suspect)

@app.delete("/suspects", tags=['Suppression'], description="Operations de suppression")
async def deleteSuspect(suspect : SuspectModel):
    return SuspectsController.delete(suspect.id)


if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)