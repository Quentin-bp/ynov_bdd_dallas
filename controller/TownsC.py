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

            return "Town Added"

        except Exception as e:
            print(f'Erreur_TownsC.insertOne() ::: {e}')

        return None


    @staticmethod
    def update(town : TownModel):

        dao = TownsDAO()
        try:
            townUpdated = Towns()

            townUpdated.setID(town.id)
            townUpdated.setName(town.name)
            townUpdated.setAddressCode(town.address_code)
            
            res: int = dao.update(town.id,townUpdated)

            if res==0:
                return "ERROR"

            return "Town Updated"

        except Exception as e:
            print(f'Erreur_TownsC.update() ::: {e}')

        return None
    

    @staticmethod
    def delete(id):
        try:

            dao = TownsDAO()

            res: int = dao.delete(id)

            if res==0 :
                return "ERROR"

            return "Town deleted"

        except Exception as e:
            print(f'Erreur_TownsC.delete() ::: {e}')

        return None