from ModelM import Model 
from TownsM import Towns
from NationalitiesM import Nationalities
class Persons(Model):

    def __init__(self):
        self.last_name: str = ""
        self.first_name: str = ""
        self.genre : int = None
        self.address : str = ""
        self.town_id : Towns = None
        self.nationality_id : Nationalities = None

    def setLastName(self, _last_name: str) -> None:
        self.last_name = _last_name

    def getLastName(self) -> str:
        return self.last_name


    def setFirstName(self, _first_name: str) -> None:
        self.first_name = _first_name

    def getFirstName(self) -> str:
        return self.first_name
    

    def setGenre(self, _genre: str) -> None:
        self.genre = _genre

    def getGenre(self) -> str:
        return self.genre
    

    def setAddress(self, _address: str) -> None:
        self.address = _address

    def getAddress(self) -> str:
        return self.address
    
    def setTownID(self, _town_id: Towns ) -> None:
        self.town_id = _town_id

    def getTownID(self) -> Towns:
        return self.town_id
    
    def setNationalityID(self, _nationality_id: Nationalities ) -> None:
        self.nationality_id = _nationality_id

    def getNationalityID(self) -> Nationalities:
        return self.town_id