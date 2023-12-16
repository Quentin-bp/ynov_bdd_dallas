from model.SuspectsM import Suspect, SuspectModel
from dao.SuspectsDAO import SuspectsDAO
from dao.PersonsDAO import PersonsDAO

class SuspectsController:

    @staticmethod
    def findById(id):
        try:
            dao = SuspectsDAO()
            suspect = dao.findById(id)

            if suspect==None:
                return "Suspects not found"
            return suspect
        except Exception as e:
            print(f"Erreur_SuspectController.findById() ::: {e}")


    @staticmethod
    def findAll():
        try:
            dao = SuspectsDAO()

            list_suspects = dao.findAll()

            if len(list_suspects)==0:
                return "There is no Suspects in database"
            return list_suspects
        except Exception as e:
            print(f"Erreur_SuspectController.findAll() ::: {e}")


    @staticmethod
    def insertOne(suspect: SuspectModel):
        
        dao = SuspectsDAO()
        daoPerson = PersonsDAO()
        try:
            person = daoPerson.findById(suspect.person_id)
            if not person:
                return 'This person_id does not exists in database'
                
            newSuspect = Suspect()

            newSuspect.setPerson(person)
            newSuspect.setVerdict(suspect.verdict)
            
            res: int = dao.insertOne(newSuspect)

            if res == 0:
                return 'ERROR'

            return "Suspect added"
        except Exception as e:
            print(f"Erreur_SuspectController.insertOne() ::: {e}")

    
    @staticmethod
    def update(suspect: SuspectModel):

        dao = SuspectsDAO()
        daoPerson = PersonsDAO()
        try:
            person = daoPerson.findById(suspect.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
                
            updatedSuspect = Suspect()

            updatedSuspect.setPerson(person)
            updatedSuspect.setSerialNumbers(suspect.verdict)
            
            res: int = dao.update(updatedSuspect)

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