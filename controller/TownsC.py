from dao.TownsDAO import TownsDAO
from model.TownsM import Towns,TownModel

class TownsController:

    @staticmethod
    def findAll():
        try:

            dao = TownsDAO()
            towns: list[Towns] = dao.findAll()

            if towns==None :
                return "ERROR"

            return towns

        except Exception as e:
            print(f'Erreur_TownsC.findAll() ::: {e}')

        return None

    @staticmethod
    def insertOne(town : TownModel):

        dao = TownsDAO()
        try:
            newTown = Towns()

            newTown.setName(town.name)
            newTown.setAddressCode(town.address_code)
            
            res: int = dao.insertOne(newTown)

            if res==0:
                return "ERROR"

            return "AJOUT BP AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_TownsC.insertOne() ::: {e}')

        return None
