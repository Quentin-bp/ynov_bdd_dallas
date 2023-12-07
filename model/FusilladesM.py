from datetime import datetime
from ModelM import ModelM 
from TownsM import TownM 

class FusilladeM(ModelM):

    def __init__(self):
        self.__adress : str = ""
        self.__town_id : TownM = None
        self.__description : str = ""
        self.__date : datetime = None
       

    def setAddress(self, address: str) -> None:
        self.__adress = address

    def getAddress(self) -> str:
        return self.__adress
    
    def setTownID(self, town_id: TownM) -> None:
        self.__town_id = town_id

    def getTownID(self) -> TownM:
        return self.__town_id
    
    def setDate(self, date: datetime) -> None:
        self.__date = date

    def getDate(self) -> datetime:
        return self.__date
    
    def setDescription(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description
