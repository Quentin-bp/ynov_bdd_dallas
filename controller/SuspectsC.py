from model.SuspectsM import Suspect, SuspectModel
from dao.SuspectsDAO import SuspectsDAO
from dao.PersonsDAO import PersonsDAO

class SuspectsController:

    @staticmethod
    def findById(id):
        try:
            S = SuspectsDAO().findById(id)

            if S==None:
                return "Suspects not found"
            return S
        except Exception as e:
            print(f"Erreur_SuspectController.findById() ::: {e}")


    @staticmethod
    def findAll():
        try:
            list_suspects = SuspectsDAO().findAll(id)

            if len(list_suspects)==0:
                return "There is no Policemen in database"
            return list_suspects
        except Exception as e:
            print(f"Erreur_SuspectController.findAll() ::: {e}")


    @staticmethod
    def insertOne(S: SuspectModel):
        
        dao = SuspectsDAO()
        daoPerson = PersonsDAO()
        try:
            person = daoPerson.findById(S.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
                
            newS = Suspect()

            newS.setPerson(person)
            newS.setVerdict(S.verdict)
            
            res: int = dao.insertOne(newSuspects)

            if res == 0:
                return 'ERROR'

            return "Suspects added"
        except Exception as e:
            print(f"Erreur_SuspectController.insertOne() ::: {e}")

    
    @staticmethod
    def update(S: SuspectModel):

        dao = SuspectsDAO()
        daoPerson = PersonsDAO()
        try:
            person = daoPerson.findById(S.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
                
            updatedS = Suspects()

            updatedS.setPerson(person)
            updatedS.setSerialNumbers(S.verdict)
            
            res: int = dao.update(newS)

            if res == 0:
                return 'ERROR'

            return "Suspects data updated"
        except Exception as e:
            print(f"Erreeu_SuspectController.update() ::: {e}")

    
    @staticmethod
    def delete(id):
        try:
            res: int = SuspectsDAO().delete(id)
            if res==0:
                return "ERROR"
            return "Suspects deleted"
        except Exception as e:
            print(f"Erreeu_SuspectController.delete() ::: {e}")
            return None