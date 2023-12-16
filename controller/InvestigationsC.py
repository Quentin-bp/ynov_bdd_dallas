from dao.InvestigationsDAO import InvestigationsDAO
from model import InvestigationsM
from model.InvestigationsM import Investigation,InvestigationModel
from dao.FusilladesDAO import FusilladesDAO

class InvestigationsController:

    @staticmethod
    def findAll():
        try:
            dao = InvestigationsDAO()
            investigation = dao.findAll()

            if investigation == None:
                print("There is no investigations in database")
            return investigation

        except Exception as e:
            print(f"Erreur_InvestigationsC.findAll() ::: {e}")
        return None

    @staticmethod
    def findById(id : int):
        try:
            dao = InvestigationsDAO()
            investigation: Investigation = dao.findById(id)

            if investigation == None:
                print("Investigations not found")
            return investigation

        except Exception as e:
            print(f"Erreur_InvestigationsC.findById() ::: {e}")
        return None

    @staticmethod
    def insertOne(investigation : InvestigationModel):
        daoFusillade = FusilladesDAO()
        dao = InvestigationsDAO()
        try:
            fusillade = daoFusillade.findById(investigation.fusillade_id)
            newInvestigation = InvestigationsM.Investigation()
            newInvestigation.setID(id)
            newInvestigation.setFusillade(fusillade)
            newInvestigation.setAdvancement(investigation.advancement)
            newInvestigation.setStatus(investigation.status)

            res: int = dao.insertOne(newInvestigation)

            if res == 0:
                return "ERROR"

            return "Investigation Added"

        except Exception as e:
            print(f"Erreur_InvestigationsC.insertOne():::{e}")
        return None

    @staticmethod
    def update(id : int, investigation : InvestigationModel):
        dao = InvestigationsDAO()
        daoFusillade = FusilladesDAO() 
        try:
            investigationUpdated = Investigation()
            fusillade = daoFusillade.findById(investigation.fusillade_id)
            if (fusillade == None):
                return 'This fusillade does not exists in database'
            investigationUpdated.setID(id)
            investigationUpdated.setFusillade(fusillade)
            investigationUpdated.setAdvancement(investigation.advancement)
            investigationUpdated.setStatus(investigation.status)

            res: int = dao.update(id, investigationUpdated)
            if res == 0:
                return "ERROR"
            return "Investigation Updated"
        except Exception as e:
            print(f"Erreur_InvestigationsC.update():::{e}")
        return None

    @staticmethod
    def delete(id : int):
        try:
            dao = InvestigationsDAO()

            res: int = dao.delete(id)
            if res == 0:
                return "ERROR"
            return "Investigation Deleted"
        except Exception as e:
            print(f"Erreur_InvestigationsC.delete():::{e}")
        return None

    
    @staticmethod
    def solveInvestigation(id):
        try:
            dao = InvestigationsDAO()
            investigation = dao.findById(id)
            if (investigation is None):
                return 'This investigation does not exists in database'
            res: int = dao.solveInvestigation(investigation)
            if res==0 :
                return "ERROR"
            return "Investigation solved"
        except Exception as e:
            print(f'Erreur_InvestigationsC.delete() ::: {e}')
        return None
    
    @staticmethod
    def getActorsByInvestigationId(id : int):
        try:
            dao = InvestigationsDAO()

            res: list[InvestigationsM.Investigation()] = dao.getActorsByInvestigationId(id)
            if res == None:
                return "ERROR"

            return res
        except Exception as e:
            print(f'Erreur_InvestigationsC.linkActorsBy_investigationId():::{e}')

        return None


    @staticmethod
    def insertOneByCommissar(user, id, fusillade_id, advancement, status):
        try:
            if user['role'] != 'commissar':
                print("Insufficient permissions.")
                return "ERROR"

            dao = InvestigationsDAO()
            new_investigation = InvestigationsM.Investigation()

            new_investigation.setID(id)
            new_investigation.setFusillade(fusillade_id)
            new_investigation.setAdvancement(advancement)
            new_investigation.setStatus(status)

            res = dao.insertOne(new_investigation)

            if res == 0:
                return "ERROR"

            return "Investigation Added"

        except Exception as e:
            print(f"Error_InvestigationsC.insert_one():::{e}")
            return None


    @staticmethod
    def findByNameAndRole(last_name:str, first_name:str, role:str):
        try:
            dao = InvestigationsDAO()

            res: list = dao.findByNameAndRole(last_name, first_name, role)
            if res == None:
                return 'ERROR'

            return res
        except Exception as e:
            #raise e
            print(f"Erreur_InvestigationsController.findByNameAndRole() ::: {e}")

