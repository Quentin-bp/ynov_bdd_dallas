from model.PersonsM import Person 
from pydantic import BaseModel

class Suspect:
    """
    Classe qui représente le schema de la table Suspects.
    """
    def __init__(self):
        self.__id: int = None
        self.__person: Person = None
        self.__verdict: str = ""   

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id

    def setVerdict(self, verdict: str) -> None:
        self.__verdict= verdict

    def getVerdict(self) -> str:
        return self.__verdict
    
    def setPerson(self, person: Person) -> None:
        self.__person= person

    def getPerson(self) -> Person:
        return self.__person


class SuspectModel(BaseModel):
    person_id : int
    verdict : str