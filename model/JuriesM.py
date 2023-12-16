from model.PersonsM import Person
from pydantic import BaseModel

class Jury:
    """
    Classe qui représente le schema de la table Juries.
    """
    def __init__(self):
        self.__id : int = None
        self.__person_id : Person = None
    
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id

    def setPersonID(self, person_id: Person) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> Person:
        return self.__person_id

class JuryModel(BaseModel):
    id : int
    person_id : int