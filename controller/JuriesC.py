from dao.JuriesDAO import JuriesDAO
from model.JuriesM import Jury,JuryModel
from dao.PersonsDAO import PersonsDAO

class JuriesController:
    @staticmethod
    def findAll():
        try:
            dao = JuriesDAO()
            list_juries: list[Jury] = dao.findAll()

            if list_juries == None:
                print("There is no jury in database")
            return list_juries

        except Exception as e:
            print(f"Erreur_JuriesC.findAll() ::: {e}")
        return None

    @staticmethod
    def findById(id : int):
        try:
            jury = JuriesDAO().findById(id)

            if jury == None:
                print("Jury not found")
            return jury

        except Exception as e:
            print(f"Erreur_JuriesC.findById() ::: {e}")
        return None

    @staticmethod
    def insertOne(jury : JuryModel):
        try:
            dao = JuriesDAO()
            daoPerson = PersonsDAO()
            newJury = Jury()
            person = daoPerson.findById(jury.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
            newJury.setPerson(person)

            res: int = dao.insertOne(newJury)

            if res == 0:
                return "ERROR"

            return "Jury Added"

        except Exception as e:
            print(f"Erreur_JuriesC.insertOne():::{e}")
        return None

    @staticmethod
    def update(id: int, jury: Jury):
        try:
            dao = JuriesDAO() 
            daoPerson = PersonsDAO()
            person = daoPerson.findById(jury.person_id)
            if (person == None):
                return 'This person_id does not exists in database'
            juryUpdated = Jury()

            juryUpdated.setID(id)
            juryUpdated.setPerson(person)

            res: int = dao.update(id, juryUpdated)
            if res == 0:
                return "ERROR"

            return "Jury Updated"

        except Exception as e:
            print(f"Erreur_JuriesC.update():::{e}")
        return None

    @staticmethod
    def delete(id : int):
        try:
            dao = JuriesDAO()

            res: int = dao.delete(id)
            if res == 0:
                return "ERROR"

            return "Jury Deleted"

        except Exception as e:
            print(f"Erreur_JuriesC.delete():::{e}")
        return None