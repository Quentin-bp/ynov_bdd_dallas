from dao.ModelDAO import ModelDAO
from model import NationalitiesM
from model.NationalitiesM import Nationality, NationalityModel
from dao.NationalitiesDAO import NationalitiesDAO

class NationalitiesController:

    @staticmethod
    def findAll():
        try:
            dao = NationalitiesDAO()
            nationality = list[Nationality] = dao.findAll()

            if nationality is not None:
                print("Nationality Unavailable")
                return nationality

        except Exception as e:
            print(f"Erreur_NationalitiesC.findAll():::{e}")
        return None

    @staticmethod
    def findById(id):
        try:
            dao = NationalitiesDAO()
            nationality: Nationality = dao.findById(id)

            if nationality == None:
                print("Nationality not found")
            return nationality

        except Exception as e:
            print(f"Erreur_NationalitiesC.findById():::{e}")
        return None

    @staticmethod
    def insertOne(nationality: NationalityModel):
        try:
            dao = NationalitiesDAO()
            newNationality = NationalitiesM.Nationality()

            newNationality.setID(nationality.id)
            newNationality.setName(nationality.name)

            res: int = dao.insertOne(newNationality)
            if res == 0:
                return "ERROR"
            return "Nationality Added"

        except Exception as e:
            print(f"Erreur_NationalitiesC.insertOne():::{e}")
        return None

    @staticmethod
    def update(nationality: NationalityModel):
        try:
            dao = NationalitiesDAO()

            nationalityUpdated = Nationality()

            nationalityUpdated.setID(nationality.id)
            nationalityUpdated.setName(nationality.name)

            res: int = dao.update(nationality.id, nationalityUpdated)
            if res == None:
                return "ERROR"
            return "Nationality Updated"

        except Exception as e:
            print(f"Erreur_NationalitiesC.update():::{e}")
        return None

    @staticmethod
    def delete(id):
        try:
            dao = NationalitiesDAO()

            res: int = dao.delete(id)
            if res == 0:
                return "ERROR"
            return "Nationality Deleted"

        except Exception as e:
            print(f"Erreur_NationalitiesC.delete():::{e}")

        return None