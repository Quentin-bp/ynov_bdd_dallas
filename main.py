from fastapi import FastAPI
import uvicorn
from controller.Investigation_PolicemenC import Investigation_PolicemenController
from controller.Investigation_SuspectsC import Investigation_SuspectsController
from controller.Investigation_JuriesC import Investigation_JuriesController
from controller.DatabaseC import DatabaseController
from controller.TownsC import TownsController
from controller.InvestigationsC import InvestigationsController
from controller.NationalitiesC import NationalitiesController
from controller.FusilladesC import FusilladesController
from controller.PersonsC import PersonsController
from controller.PolicemenC import PolicemenController
from controller.SuspectsC import SuspectsController
from model.TownsM import TownModel
from model.NationalitiesM import NationalityModel
from model.JuriesM import JuryModel
from model.InvestigationsM import InvestigationModel
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

############### Associations #####################################
@app.post("/Investigation_Policemen/{investigation_id}/{policeman_id}", tags=['Associations'])
async def createInvestigationPolicemen(investigation_id:int, policeman_id:int):
    return Investigation_PolicemenController.insertOne(investigation_id, policeman_id)

@app.post("/Investigation_suspects/{investigation_id}/{suspect_id}", tags=['Associations'])
async def createInvestigationSuspects(investigation_id:int, suspect_id:int):
    return Investigation_SuspectsController.insertOne(investigation_id, suspect_id)

@app.post("/Investigation_Juries/{investigation_id}/{jury_id}", tags=['Associations'])
async def createInvestigationJuries(investigation_id:int, jury_id:int):
    return Investigation_JuriesController.insertOne(investigation_id, jury_id)

################# Nationalities #############################################

@app.get("/Nationalities", tags=['Nationalities'], description="Operations sur la table nationalité")
async def getNationalities():
    return NationalitiesController.findAll()

@app.get("/Nationalities/{id}", tags=['Nationalities'], description="Operations sur la table nationalité")
async def getNationality(id):
    return NationalitiesController.findById(id)

@app.post("/Nationalities", tags=['Nationalities'], description="Operations sur la table nationalité")
async def createNationality(nationality : NationalityModel):
    return NationalitiesController.insertOne(nationality)

@app.put("/Nationalities", tags=['Nationalities'], description="Operations sur la table nationalité")
async def updateNationality(nationality : NationalityModel):
    return NationalitiesController.update(nationality)

@app.delete("/Nationalities", tags=['Nationalities'], description="Operations sur la table nationalité")
async def deleteNationality(nationality : NationalityModel):
    return NationalitiesController.delete(nationality.id)


################# Towns #############################################

@app.get("/towns", tags=['Towns'], description="Operations sur la table villes")
async def getTowns():
    return TownsController.findAll()

@app.get("/town/{id}", tags=['Towns'], description="Operations sur la table villes")
async def getTown(id):
    return TownsController.findById(id)

@app.post("/town", tags=['Towns'], description="Operations sur la table villes")
async def createTown(town : TownModel):
    return TownsController.insertOne(town)

@app.put("/town", tags=['Towns'], description="Operations sur la table villes")
async def updateTown(town : TownModel):
    return TownsController.update(town)

@app.delete("/town", tags=['Towns'], description="Operations sur la table villes")
async def deleteTown(town : TownModel):
    return TownsController.delete(town.id)


################# Fusillades #############################################

@app.get("/fusillades", tags=['Fusillades'], description="Operations sur la table fusillades")
async def getFusillades():
    return FusilladesController.findAll()

@app.get("/fusillade/{id}", tags=['Fusillades'], description="Operations sur la table fusillades")
async def getFusillade(id):
    return FusilladesController.findById(id)

@app.post("/fusillade", tags=['Fusillades'], description="Operations sur la table fusillades")
async def createFusillade(fusillade : FusilladeModel):
    return FusilladesController.insertOne(fusillade)

@app.put("/fusillade", tags=['Fusillades'], description="Operations sur la table fusillades")
async def updateFusillade(fusillade : FusilladeModel):
    return FusilladesController.update(fusillade)

@app.delete("/fusillade", tags=['Fusillades'], description="Operations sur la table fusillades")
async def deleteFusillade(fusillade : FusilladeModel):
    return FusilladesController.delete(fusillade.id)


################## Persons ################################
@app.get("/persons", tags=['Persons'], description="Operations sur la table persons")
async def getPersons():
    return PersonsController.findAll()

@app.get("/persons/{id}", tags=['Persons'], description="Operations sur la table persons")
async def getPerson(id: int):
    return PersonsController.findById(id)

@app.post("/persons", tags=['Persons'], description="Operations sur la table persons")
async def createPerson(person : PersonModel):
    return PersonsController.insertOne(person)

@app.put("/persons", tags=['Persons'], description="Operations sur la table persons")
async def updatePerson(person : PersonModel):
    return PersonsController.update(person)

@app.delete("/persons", tags=['Persons'], description="Operations sur la table persons")
async def deletePerson(person : PersonModel):
    return PersonsController.delete(person.id)


################## Policemen ################################
@app.get("/policemen", tags=['Policemen'], description="Operations sur la table policemen")
async def getPolicemen():
    return PolicemenController.findAll()

@app.get("/policemen/{id}", tags=['Policemen'], description="Operations sur la table policemen")
async def getPoliceman(id):
    return PolicemenController.findById(id)

@app.post("/policemen", tags=['Policemen'], description="Operations sur la table policemen")
async def createPoliceman(policeman : PolicemanModel):
    return PolicemenController.insertOne(policeman)

@app.put("/policemen", tags=['Policemen'], description="Operations sur la table policemen")
async def updatePoliceman(policeman : PolicemanModel):
    return PolicemenController.update(policeman)

@app.delete("/policemen", tags=['Policemen'], description="Operations sur la table policemen")
async def deletePoliceman(policeman : PolicemanModel):
    return PolicemenController.delete(policeman.id)

################## Suspects ################################
@app.get("/suspects", tags=['Suspects'], description="Operations sur la table suspects")
async def getSuspects():
    return SuspectsController.findAll()

@app.get("/suspects/{id}", tags=['Suspects'], description="Operations sur la table suspects")
async def getSuspect(id):
    return SuspectsController.findById(id)

@app.post("/suspects", tags=['Suspects'], description="Operations sur la table suspects")
async def createSuspect(suspect : SuspectModel):
    return SuspectsController.insertOne(suspect)

@app.put("/suspects", tags=['Suspects'], description="Operations sur la table suspects")
async def updateSuspect(suspect : SuspectModel):
    return SuspectsController.update(suspect)

@app.delete("/suspects", tags=['Suspects'], description="Operations sur la table suspects")
async def deleteSuspect(suspect : SuspectModel):
    return SuspectsController.delete(suspect.id)


################## Juries ################################
@app.get("/juries", tags=['Juries'], description="Operations sur la table juries")
async def getJuries():
    return JuriesController.findAll()

@app.get("/juries/{id}", tags=['Juries'], description="Operations sur la table juries")
async def getJury(id):
    return JuriesController.findById(id)

@app.post("/juries", tags=['Juries'], description="Operations sur la table juries")
async def createJury(jury : JuryModel):
    return JuriesController.insertOne(jury)

@app.put("/juries", tags=['Juries'], description="Operations sur la table juries")
async def updateJury(jury : JuryModel):
    return JuriesController.update(jury)

@app.delete("/juries", tags=['Juries'], description="Operations sur la table juries")
async def deleteJury(jury : JuryModel):
    return JuriesController.delete(jury.id)


################# Investigations #############################################

@app.get("/investigation", tags=['Investigations'], description="Operations sur la table investigations")
async def getInvestigations():
    return InvestigationsController.findAll()

@app.get("/investigation/{id}", tags=['Investigations'], description="Operations sur la table investigations")
async def getInvestigation(id):
    return InvestigationsController.findById(id)

@app.post("/investigation", tags=['Investigations'], description="Operations sur la table investigations")
async def createInvestigation(investigation : InvestigationModel):
    return InvestigationsController.insertOne(investigation)

@app.put("/investigation", tags=['Investigations'], description="Operations sur la table investigations")
async def updateInvestigation(investigation : InvestigationModel):
    return InvestigationsController.update(investigation)

@app.delete("/investigation", tags=['Investigations'], description="Operations sur la table investigations")
async def deleteInvestigation(investigation : InvestigationModel):
    return InvestigationsController.delete(investigation.id)

@app.get("/investigation/{role}/{last_name}/{first_name}", tags=['Investigations'], description='Rechercher une enquête par le nom, prénom et le role de la personne')
async def findByNameAndRole(last_name:str, first_name:str, role:str):
    return InvestigationsController.findByNameAndRole(last_name, first_name, role)


if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)