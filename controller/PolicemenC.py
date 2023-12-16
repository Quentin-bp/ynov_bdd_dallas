from model.PolicemenM import Policeman, PolicemanModel
from dao.PolicemenDAO import PolicemenDAO
from dao.PersonsDAO import PersonsDAO

class PolicemenController:

    @staticmethod
    def findById(id : int):
        try:
            policeman = PolicemenDAO().findById(id)

            if policeman==None:
                return "Policeman not found"
            return policeman
        except Exception as e:
            print(f"Erreur_PolicemenController.findById() ::: {e}")


    @staticmethod
    def findAll():
        try:
            list_policemen = PolicemenDAO().findAll()

            if len(list_policemen)==0:
                return "There is no Policemen in database"
            return list_policemen
        except Exception as e:
            print(f"Erreur_PolicemenController.findAll() ::: {e}")


    @staticmethod
    def insertOne(policeman: PolicemanModel):
        
        dao = PolicemenDAO()
        daoPerson = PersonsDAO()
        try:
            person = daoPerson.findById(policeman.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
                
            newPoliceman = Policeman()

            newPoliceman.setPerson(person)
            newPoliceman.setSerialNumbers(policeman.serial_numbers)
            
            res: int = dao.insertOne(newPoliceman)

            if res == 0:
                return 'ERROR'
                
            return "Policeman added"
        except Exception as e:
            print(f"Erreur_PolicemenController.insertOne() ::: {e}")

    
    @staticmethod
    def update(id : int,policeman: PolicemanModel):

        dao = PolicemenDAO()
        daoPerson = PersonsDAO()
        try:
            person = daoPerson.findById(policeman.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
                
            updatedPoliceman = Policeman()

            updatedPoliceman.setPerson(person)
            updatedPoliceman.setSerialNumbers(policeman.serial_numbers)
            
            res: int = dao.update(id,updatedPoliceman)

            if res == 0:
                return 'ERROR'

            return "Policeman data updated"
        except Exception as e:
            print(f"Erreur_PolicemenController.update() ::: {e}")

    
    @staticmethod
    def delete(id : int):
        try:
            res: int = PolicemenDAO().delete(id)
            if res==0:
                return "ERROR"
            return "Policeman deleted"
        except Exception as e:
            print(f"Erreur_PolicemenController.delete() ::: {e}")
            return None