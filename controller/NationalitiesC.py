from dao.ModelDAO import ModelDAO
from model import NationalitiesM
from model.NationalitiesM import Nationality
from dao.NationalitiesDAO import NationalitiesDAO

class NationalitiesController:

    @staticmethod
    def findAll():
        try:
            ndao = NationalitiesDAO()
            citizen = list[Nationality] = ndao.findAll()

            if citizen == None:
                print("Nationality Unavailable")
                return citizen

        except Exception as e:
            print(f"Erreur_NationalitiesC.findAll():::{e}")
        return None

    @staticmethod
    def findById(id):
        try:
            ndao = NationalitiesDAO()
            citizen = list[Nationality] = ndao.findById(id)

            if citizen == None:
                print("Nationality not found")
            return citizen

        except Exception as e:
            print(f"Erreur_NationalitiesC.findById():::{e}")
        return None

    @staticmethod
    def insertOne(nId, nName):
        try:
            ndao = NationalitiesDAO()
            newNationality = NationalitiesM.Nationality()

            newNationality.setID(nId)
            newNationality.setName(nName)

            res: int = ndao.insertOne(newNationality)
            if res == 0:
                return "ERROR"
            return "Nationality Added"

        except Exception as e:
            print(f"Erreur_NationalitiesC.insertOne():::{e}")
        return None

    @staticmethod
    def update(nId, nName):
        try:
            ndao = NationalitiesDAO()

            nationalityUpdated = Nationality()

            nationalityUpdated.setID(nId)
            nationalityUpdated.setName(nName)

            res: int = ndao.update(nId, nName)
            if res == None:
                return "ERROR"
            return "Nationality Updated"

        except Exception as e:
            print(f"Erreur_NationalitiesC.update():::{e}")
        return None

    @staticmethod
    def delete(id):
        try:
            ndao = NationalitiesDAO()

            res: int = ndao.delete(id)
            if res == 0:
                return "ERROR"
            return "Nationality Deleted"

        except Exception as e:
            print(f"Erreur_NationalitiesC.delete():::{e}")

        return None