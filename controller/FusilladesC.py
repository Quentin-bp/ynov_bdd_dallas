from dao.FusilladesDAO import FusilladesDAO
from model.FusilladesM import Fusillade ,FusilladeModel
from dao.TownsDAO import TownsDAO
from datetime import datetime
class FusilladesController:

    
    @staticmethod
    def findAll():
        try:

            dao = FusilladesDAO()
            towns: list[Fusillade] = dao.findAll()

            if towns==None :
                return "There is no fusillades in database"

            return towns

        except Exception as e:
            print(f'Erreur_FusilladesC.findAll() ::: {e}')

        return None
    
    @staticmethod
    def findById(id : int):
        try:

            dao = FusilladesDAO()
            fusillade: Fusillade = dao.findById(id)

            if fusillade==None :
                return "Fusillade not found"

            return fusillade

        except Exception as e:
            print(f'Erreur_FusilladesC.findById() ::: {e}')

        return None
    
    @staticmethod
    def insertOne(fusillade : FusilladeModel):

        daoFusillade = FusilladesDAO()
        daoTown= TownsDAO()
        try:
            town = daoTown.findById(fusillade.town_id)
            if (town == None) :
                return "Fusillade id not found"
            newFusillade = Fusillade()

            newFusillade.setStreetNumber(fusillade.street_number)
            newFusillade.setStreetName(fusillade.street_name)
            newFusillade.setAdditionalAddress(fusillade.additional_address)
            newFusillade.setDescription(fusillade.description)
            newFusillade.setDate(datetime.strptime(fusillade.date, "%Y-%m-%d").date())
            newFusillade.setTown(town)

            res: int = daoFusillade.insertOne(newFusillade)

            if res==0:
                return "ERROR"

            return "Fusillade Added"

        except Exception as e:
            print(f'Erreur_FusilladesC.insertOne() ::: {e}')

        return None


    @staticmethod
    def update(id : int,fusillade : FusilladeModel):
        daoFusillade = FusilladesDAO()
        daoTown= TownsDAO()
        try:
            town = daoTown.findById(fusillade.town_id)
            fusilladeUpdated = Fusillade()
            fusilladeUpdated.setID(id)
            fusilladeUpdated.setStreetNumber(fusillade.street_number)
            fusilladeUpdated.setStreetName(fusillade.street_name)
            fusilladeUpdated.setAdditionalAddress(fusillade.additional_address)
            fusilladeUpdated.setDescription(fusillade.description)
            fusilladeUpdated.setDate(datetime.strptime(fusillade.date, "%Y-%m-%d").date())
            fusilladeUpdated.setTown(town)
            
            res: int = daoFusillade.update(id,fusilladeUpdated)
            if res==0:
                return "ERROR"
            return "Fusillade Updated"
        except Exception as e:
            print(f'Erreur_FusilladesC.update() ::: {e}')
        return None
    
    @staticmethod
    def delete(id : int):
        try:
            dao = FusilladesDAO()
            res: int = dao.delete(id)
            if res==0 :
                return "ERROR"
            return "Fusillade deleted"
        except Exception as e:
            print(f'Erreur_FusilladesC.delete() ::: {e}')
        return None