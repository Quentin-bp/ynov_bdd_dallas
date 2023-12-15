from dao.JuriesDAO import JuriesDAO
from model.JuriesM import Juries
from dao.PersonsDAO import PersonsDAO
from model import JuriesM

class JuriesController:
    @staticmethod
    def findAll():
        try:
            dao = JuriesDAO()
            person: list[Juries] = dao.findAll()

            if person == None:
                print("There is no jury in database")
            return person

        except Exception as e:
            print(f"Erreur_JuriesC.findAll() ::: {e}")
        return None

    @staticmethod
    def findById(id):
        try:

            jury = JuriesDAO.findById(id)

            if jury == None:
                print("Juries not found")
            return jury

        except Exception as e:
            print(f"Erreur_JuriesC.findById() ::: {e}")
        return None

    @staticmethod
    def insertOne(id, person_id):
        try:
            dao = JuriesDAO()
            newJury = JuriesM.Juries()

            newJury.setID(id)
            newJury.setPerson(person_id)

            res: int = dao.insertOne(newJury)

            if res == 0:
                return "ERROR"

            return "Jury Added"

        except Exception as e:
            print(f"Erreur_JuriesC.insertOne():::{e}")
        return None

    @staticmethod
    def update(id, person_id):
        try:
            dao = JuriesDAO()

            juryUpdated = Juries()

            juryUpdated.setID(id)
            juryUpdated.setPerson(person_id)

            res: int = dao.update(id, juryUpdated)
            if res == 0:
                return "ERROR"

            return "Jury Updated"

        except Exception as e:
            print(f"Erreur_JuriesC.update():::{e}")
        return None

    @staticmethod
    def delete(id):
        try:
            dao = JuriesDAO()

            res: int = dao.delete(id)
            if res == 0:
                return "ERROR"

            return "Jury Deleted"

        except Exception as e:
            print(f"Erreur_JuriesC.delete():::{e}")
        return None