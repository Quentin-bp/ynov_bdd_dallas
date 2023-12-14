from model.PersonsM import Person 
from pydantic import BaseModel

class Policeman:
    """
    Classe qui représente le schema de la table Policemen.
    """
    def __init__(self):
        self.__id: int = None
        self.__person : Person = None
        self.__serial_numbers : str = ""
        
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id
    
    def setSerialNumbers(self, serial_numbers: str) -> None:
        self.__serial_numbers = serial_numbers

    def getSerialNumbers(self) -> str:
        return self.__serial_numbers
    
    def setPerson(self, person: Person) -> None:
        self.__person = person

    def getPerson(self) -> Person:
        return self.__person


class PolicemanModel(BaseModel):
    id : int
    person_id : int
    serial_numbers : str
