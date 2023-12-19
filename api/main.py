from fastapi import FastAPI
import uvicorn
from controller.InvestigationPolicemenC import InvestigationPolicemenController
from controller.InvestigationSuspectsC import InvestigationSuspectsController
from controller.InvestigationJuriesC import InvestigationJuriesController
from controller.DatabaseC import DatabaseController
from controller.TownsC import TownsController
from controller.InvestigationsC import InvestigationsController
from controller.NationalitiesC import NationalitiesController
from controller.FusilladesC import FusilladesController
from controller.PersonsC import PersonsController
from controller.PolicemenC import PolicemenController
from controller.SuspectsC import SuspectsController
from controller.JuriesC import JuriesController

from model.TownsM import TownModel
from model.NationalitiesM import NationalityModel
from model.InvestigationsM import InvestigationModel
from model.FusilladesM import FusilladeModel
from model.PersonsM import PersonModel
from model.PolicemenM import PolicemanModel
from model.SuspectsM import SuspectModel
from model.JuriesM import JuryModel
from model.InvestigationsPersonsM import InvestigationSuspect, InvestigationPoliceman, InvestigationJury, InvestigationResearch
app = FastAPI()
descriptionGeneral = "Operations on the table"

@app.get("/", tags=['Init'])
async def start():
    return {"Init msg": "Welcome to Dallas !"}

################# BDD #############################################

@app.get("/create_database", tags=['BDD'])
async def createDatabase():
    return DatabaseController.createDatabase()
@app.get("/insert_data", tags=['BDD'])
async def insertData():
    return DatabaseController.insertData()

################# Nationalities #############################################
nationalitiesTag = "Nationalities"
@app.get("/nationalities", tags=[nationalitiesTag], description=descriptionGeneral + nationalitiesTag)
async def getNationalities():
    return NationalitiesController.findAll()

@app.get("/nationality/{id}", tags=[nationalitiesTag], description=descriptionGeneral + nationalitiesTag)
async def getNationality(id):
    return NationalitiesController.findById(id)

@app.post("/nationality", tags=[nationalitiesTag], description=descriptionGeneral + nationalitiesTag)
async def createNationality(nationality : NationalityModel):
    return NationalitiesController.insertOne(nationality)

@app.put("/nationality/{id}", tags=[nationalitiesTag], description=descriptionGeneral + nationalitiesTag)
async def updateNationality(id : int,nationality : NationalityModel):
    return NationalitiesController.update(id,nationality)

@app.delete("/nationality/{id}", tags=[nationalitiesTag], description=descriptionGeneral + nationalitiesTag)
async def deleteNationality(id : int):
    return NationalitiesController.delete(id)


################# Towns #############################################

townsTag = "Towns"
@app.get("/towns", tags=[townsTag], description=descriptionGeneral + townsTag)
async def getTowns():
    return TownsController.findAll()

@app.get("/town/{id}", tags=[townsTag], description=descriptionGeneral + townsTag)
async def getTown(id):
    return TownsController.findById(id)

@app.post("/town", tags=[townsTag], description=descriptionGeneral + townsTag)
async def createTown(town : TownModel):
    return TownsController.insertOne(town)

@app.put("/town/{id}", tags=[townsTag], description=descriptionGeneral + townsTag)
async def updateTown(id : int,town : TownModel):
    return TownsController.update(id, town)

@app.delete("/town/{id}", tags=[townsTag], description=descriptionGeneral + townsTag)
async def deleteTown(id : int):
    return TownsController.delete(id)


################# Fusillades #############################################
fusilladesTag = "Fusillades"
@app.get("/fusillades", tags=[fusilladesTag], description=descriptionGeneral + fusilladesTag)
async def getFusillades():
    return FusilladesController.findAll()

@app.get("/fusillade/{id}", tags=[fusilladesTag], description=descriptionGeneral + fusilladesTag)
async def getFusillade(id):
    return FusilladesController.findById(id)

@app.post("/fusillade", tags=[fusilladesTag], description=descriptionGeneral + fusilladesTag)
async def createFusillade(fusillade : FusilladeModel):
    return FusilladesController.insertOne(fusillade)

@app.put("/fusillade/{id}", tags=[fusilladesTag], description=descriptionGeneral + fusilladesTag)
async def updateFusillade(id : int,fusillade : FusilladeModel):
    return FusilladesController.update(id,fusillade)

@app.delete("/fusillade/{id}", tags=[fusilladesTag], description=descriptionGeneral + fusilladesTag)
async def deleteFusillade(id: int):
    return FusilladesController.delete(id)


################## Persons ################################
personsTag = "Persons"
@app.get("/persons", tags=[personsTag], description=descriptionGeneral + personsTag)
async def getPersons():
    return PersonsController.findAll()

@app.get("/person/{id}", tags=[personsTag], description=descriptionGeneral + personsTag)
async def getPerson(id: int):
    return PersonsController.findById(id)

@app.post("/person", tags=[personsTag], description=descriptionGeneral + personsTag)
async def createPerson(person : PersonModel):
    return PersonsController.insertOne(person)

@app.put("/person/{id}", tags=[personsTag], description=descriptionGeneral + personsTag)
async def updatePerson(id: int,person : PersonModel):
    return PersonsController.update(id,person)

@app.delete("/person/{id}", tags=[personsTag], description=descriptionGeneral + personsTag)
async def deletePerson(id: int):
    return PersonsController.delete(id)


################## Policemen ################################
policemenTag = "Policemen"
@app.get("/policemen", tags=[policemenTag], description=descriptionGeneral + policemenTag)
async def getPolicemen():
    return PolicemenController.findAll()

@app.get("/policeman/{id}", tags=[policemenTag], description=descriptionGeneral + policemenTag)
async def getPoliceman(id):
    return PolicemenController.findById(id)

@app.post("/policeman", tags=[policemenTag], description=descriptionGeneral + policemenTag)
async def createPoliceman(policeman : PolicemanModel):
    return PolicemenController.insertOne(policeman)

@app.put("/policeman/{id}", tags=[policemenTag], description=descriptionGeneral + policemenTag)
async def updatePoliceman(id : int,policeman : PolicemanModel):
    return PolicemenController.update(id, policeman)

@app.delete("/policeman/{id}", tags=[policemenTag], description=descriptionGeneral + policemenTag)
async def deletePoliceman(id : int):
    return PolicemenController.delete(id)

################## Suspects ################################
suspectsTag = "Suspects"
@app.get("/suspects", tags=[suspectsTag], description=descriptionGeneral + suspectsTag)
async def getSuspects():
    return SuspectsController.findAll()

@app.get("/suspect/{id}", tags=[suspectsTag], description=descriptionGeneral + suspectsTag)
async def getSuspect(id):
    return SuspectsController.findById(id)

@app.post("/suspect", tags=[suspectsTag], description=descriptionGeneral + suspectsTag)
async def createSuspect(suspect : SuspectModel):
    return SuspectsController.insertOne(suspect)

@app.put("/suspect/{id}", tags=[suspectsTag], description=descriptionGeneral + suspectsTag)
async def updateSuspect(id : int,suspect : SuspectModel):
    return SuspectsController.update(id,suspect)

@app.delete("/suspect/{id}", tags=[suspectsTag], description=descriptionGeneral + suspectsTag)
async def deleteSuspect(id : int):
    return SuspectsController.delete(id)


################## Juries ################################
juriesTag = "Juries"
@app.get("/juries", tags=[juriesTag], description=descriptionGeneral + juriesTag)
async def getJuries():
    return JuriesController.findAll()

@app.get("/jury/{id}", tags=[juriesTag], description=descriptionGeneral + juriesTag)
async def getJury(id : int):
    return JuriesController.findById(id)

@app.post("/jury", tags=[juriesTag], description=descriptionGeneral + juriesTag)
async def createJury(jury : JuryModel):
    return JuriesController.insertOne(jury)

@app.put("/jury/{id}", tags=[juriesTag], description=descriptionGeneral + juriesTag)
async def updateJury(id : int,jury : JuryModel):
    return JuriesController.update(id,jury)

@app.delete("/jury/{id}", tags=[juriesTag], description=descriptionGeneral + juriesTag)
async def deleteJury(id : int):
    return JuriesController.delete(id)


################# Investigations #############################################
investigationsTag = "Investigations"
@app.get("/investigations", tags=[investigationsTag], description=descriptionGeneral + investigationsTag)
async def getInvestigations():
    return InvestigationsController.findAll()

@app.get("/investigation/{id}", tags=[investigationsTag], description=descriptionGeneral + investigationsTag)
async def getInvestigation(id):
    return InvestigationsController.findById(id)

@app.post("/investigation", tags=[investigationsTag], description=descriptionGeneral + investigationsTag)
async def createInvestigation(investigation : InvestigationModel):
    return InvestigationsController.insertOne(investigation)

@app.put("/investigation/{id}", tags=[investigationsTag], description=descriptionGeneral + investigationsTag)
async def updateInvestigation(id : int,investigation : InvestigationModel):
    return InvestigationsController.update(id,investigation)

@app.delete("/investigation/{id}", tags=[investigationsTag], description=descriptionGeneral + investigationsTag)
async def deleteInvestigation(id : int):
    return InvestigationsController.delete(id)

@app.post("/investigation/research", tags=[investigationsTag], description='Rechercher une enquête par le nom, prénom et le role de la personne')
async def investigationResearch(investigationResearch: InvestigationResearch):
    return InvestigationsController.findByNameAndRole(investigationResearch.last_name, investigationResearch.first_name, investigationResearch.role)

@app.post("/solve_investigation/{id}", tags=[investigationsTag], description="Lancer la résolution d'une enquête") # pourquoi pas un get ? 
async def solveInvestigation(id):
    return InvestigationsController.solveInvestigation(id)

############### Associations #####################################
@app.post("/investigation_policemen", tags=['Associations'])
async def createInvestigationPolicemen(link : InvestigationPoliceman):
    return InvestigationPolicemenController.insertOne(link)

@app.post("/investigation_suspects", tags=['Associations'])
async def createInvestigationSuspects(link : InvestigationSuspect):
    return InvestigationSuspectsController.insertOne(link)

@app.post("/investigation_juries", tags=['Associations'])
async def createInvestigationJuries(link : InvestigationJury):
    return InvestigationJuriesController.insertOne(link)

if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)