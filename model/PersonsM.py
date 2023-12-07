from ModelM import Model 
from TownsM import Towns
from NationalitiesM import Nationalities
class Persons(Model):

    def __init__(self):
<<<<<<< HEAD
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
=======
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
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2

    def getFirstName(self) -> str:
        return self.first_name
    

<<<<<<< HEAD
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
=======
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
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2
