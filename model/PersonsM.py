from TownsM import Town
from NationalitiesM import Nationality


class Person:
    """
    Classe qui représente le schema de la table Persons.
    """
    def __init__(self):
        self.__id: int = None
        self.__firstname: str = ""
        self.__lastname: str = ""
        self.__genre : int = None
        self.__street_number : str = "" # exple 1 bis
        self.__street_name: str = ""
        self.__additional_address: str = ""
        self.__town_id : Town = None
        self.__nationality_id : Nationality = None

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setFirstName(self, firstname: str) -> None:
        self.__firstname = firstname

    def getFirstName(self) -> str:
        return self.__firstname

    def setLastName(self, lastname: str) -> None:
        self.__lastname = lastname

    def getLastName(self) -> str:
        return self.__lastname
  
    def setGenre(self, genre: str) -> None:
        self.__genre = genre

    def getGenre(self) -> str:
        return self.__genre
    
    def setStreetNumber(self, street_number: str) -> None:
        self.__street_number = street_number

    def getStreetNumber(self) -> str:
        return self.__street_number

    def setStreetName(self, street_name: str) -> None:
        self.__street_name = street_name

    def getStreetName(self) -> str:
        return self.__street_name

    def setAdditionalAddress(self, additional_address: str) -> None:
        self.__additional_address = additional_address

    def getAdditionalAddress(self) -> str:
        return self.__additional_address
    
    def setTownID(self, town_id: Town) -> None:
        self.__town_id = town_id

    def getTownID(self) -> Town:
        return self.__town_id
    
    def setNationalityID(self, nationality_id: Nationality) -> None:
        self.__nationality_id = nationality_id

    def getNationalityID(self) -> Nationality:
        return self.__nationality_id
