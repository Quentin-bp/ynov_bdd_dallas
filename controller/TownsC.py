from dao.TownsDAO import TownsDAO
from model.TownsM import Town,TownModel

class TownsController:

    @staticmethod
    def findById(id : int):
        try:

            dao = TownsDAO()
            print(id)
            town: Town = dao.findById(id)

            if town==None :
                return "Town not found"

            return town

        except Exception as e:
            print(f'Erreur_TownsC.findById() ::: {e}')

        return None
    
    @staticmethod
    def findAll():
        try:

            dao = TownsDAO()
            towns: list[Town] = dao.findAll()

            if towns==None :
                return "There is no towns in database"

            return towns

        except Exception as e:
            print(f'Erreur_TownsC.findAll() ::: {e}')

        return None

    @staticmethod
    def insertOne(town : TownModel):

        dao = TownsDAO()
        try:
            newTown = Town()

            newTown.setName(town.name)
            newTown.setPostalCode(town.postal_code)
            
            res: int = dao.insertOne(newTown)

            if res==0:
                return "ERROR"

            return "Town Added"

        except Exception as e:
            print(f'Erreur_TownsC.insertOne() ::: {e}')

        return None

    @staticmethod
    def update(id: int,town : TownModel):
        dao = TownsDAO()
        try:
            townUpdated = Town()
            townUpdated.setID(id)
            townUpdated.setName(town.name)
            townUpdated.setPostalCode(town.postal_code)
            
            res: int = dao.update(id,townUpdated)
            if res==0:
                return "ERROR"
            return "Town Updated"
        except Exception as e:
            print(f'Erreur_TownsC.update() ::: {e}')
        return None
    
    @staticmethod
    def delete(id : int):
        try:
            dao = TownsDAO()
            res: int = dao.delete(id)
            if res==0 :
                return "ERROR"
            return "Town deleted"
        except Exception as e:
            print(f'Erreur_TownsC.delete() ::: {e}')
        return None