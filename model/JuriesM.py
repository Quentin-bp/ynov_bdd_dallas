from model.PersonsM import Person
from pydantic import BaseModel

class Jury:
    """
    Classe qui représente le schema de la table Juries.
    """
    def __init__(self):
        self.__id : int = None
        self.__person : Person = None
    
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id

    def setPerson(self, person: Person) -> None:
        self.__person = person

    def getPerson(self) -> Person:
        return self.__person

class JuryModel(BaseModel):
    person_id : int