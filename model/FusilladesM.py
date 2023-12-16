from model.TownsM import Town 
from pydantic import BaseModel,validator
from datetime import date
class Fusillade:

    def __init__(self):
        self.__id : int = None
        self.__street_number : str = "" # exple 1 bis
        self.__street_name: str = ""
        self.__additional_address: str = ""
        self.__description : str = ""
        self.__date : date = None
        self.__town : Town = None

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id

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
    
    def setDate(self, date: date) -> None:
        self.__date = date

    def getDate(self) -> date:
        return self.__date
    
    def setDescription(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description


class FusilladeModel(BaseModel):
        street_number: str = ""
        street_name: str = ""
        additional_address: str = ""
        description : str = ""
        date: str = ""
        town_id : int