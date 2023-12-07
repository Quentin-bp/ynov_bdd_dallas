from ModelM import Model 
from TownsM import Towns
from NationalitiesM import Nationalities
class Persons(Model):

    def __init__(self):
        self.__last_name: str = ""
        self.__last_name: str = ""
        self.__genre : int = None
        self.__adresse : str = ""
        self.__town_id : Towns = None
        self.__nationality_id : Nationalities = None

    def setLastName(self, _last_name: str) -> None:
        self.__last_name = _last_name

    def getLastName(self) -> str:
        return self.__last_name


    def setFirstName(self, first_name: str) -> None:
        self.first_name = first_name

    def getFirstName(self) -> str:
        return self.first_name
    

    def setGenre(self, genre: str) -> None:
        self.__genre = genre

    def getGenre(self) -> str:
        return self.__genre
    

    def setAddress(self, address: str) -> None:
        self.__adresse = address

    def getAddress(self) -> str:
        return self.__adresse
    
    def setTownID(self, town_id: Towns ) -> None:
        self.__town_id = town_id

    def getTownID(self) -> Towns:
        return self.__town_id
    
    def setNationalityID(self, nationality_id: Nationalities ) -> None:
        self.__nationality_id = nationality_id

    def getNationalityID(self) -> Nationalities:
        return self.__town_id
