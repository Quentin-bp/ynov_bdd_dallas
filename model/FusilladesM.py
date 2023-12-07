import datetime
from ModelM import Model 
from TownsM import Towns 

class Fusillades(Model):

    def __init__(self):
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