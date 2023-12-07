import datetime
from ModelM import Model 
from TownsM import Towns 

class Fusillades(Model):

    def __init__(self):
<<<<<<< HEAD
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
=======
        self.address : str = ""
        self.town_id : Towns = None
        self.description : str = ""
        self.date : datetime = None
       
    def setTownID(self, _town_id: Towns ) -> None:
        self.town_id = _town_id

    def getTownID(self) -> Towns:
        return self.town_id
    
    def setAddress(self, _address: str) -> None:
        self.address = _address

    def getAddress(self) -> str:
        return self.address
    
    def setDate(self, _date: datetime ) -> None:
        self.date = _date

    def getDate(self) -> datetime:
        return self.date
    
    def setDescription(self, _description: str) -> None:
        self.description = _description

    def getDescription(self) -> str:
        return self.description
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2
