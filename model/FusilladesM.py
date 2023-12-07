import datetime
from ModelM import Model 
from TownsM import Towns 

class Fusillades(Model):

    def __init__(self):
        self.__adresse : str = ""
        self.__town_id : Towns = None
        self.__description : str = ""
        self.__date : datetime = None
       
    def setTownID(self, town_id: Towns ) -> None:
        self.__town_id = town_id

    def getTownID(self) -> Towns:
        return self.__town_id
    
    def setAddress(self, address: str) -> None:
        self.__adresse = address

    def getAddress(self) -> str:
        return self.__adresse
    
    def setDate(self, _date: datetime ) -> None:
        self.__date = _date

    def getDate(self) -> datetime:
        return self.__date
    
    def setDescription(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description