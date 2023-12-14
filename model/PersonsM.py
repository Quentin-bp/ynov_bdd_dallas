from model.TownsM import Town
from pydantic import BaseModel
from typing import Optional
from model.NationalitiesM import Nationality


class Person:
    """
    Classe qui représente le schema de la table Persons.
    """
    def __init__(self):
        self.__id: int = None
        self.__firstname: str = ""
        self.__lastname: str = ""
        self.__genre : int = None
        self.__street_number : str = "" # exple : rue 1 bis
        self.__street_name: str = ""
        self.__additional_address: str = ""
        self.__town : Town = None
        self.__nationality : Nationality = None

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
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
    
    def setTown(self, town: Town) -> None:
        self.__town = town

    def getTown(self) -> Town:
        return self.__town
    
    def setNationality(self, nationality: Nationality) -> None:
        self.__nationality = nationality

    def getNationalityID(self) -> Nationality:
        return self.__nationality


class PersonModel(BaseModel):
        id: int
        firstname: str 
        lastname: str
        genre : int
        street_number : str
        street_name: str
        additional_address: str
        town_id : int
        nationality_id : int