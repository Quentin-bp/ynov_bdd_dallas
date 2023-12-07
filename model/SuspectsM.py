from ModelM import Model 
from PersonsM import Person 
class Suspects(Model):

    def __init__(self):
        self.__person_id: Person = None
        self.__verdict: str = ""   
        
    def setVerdict(self, verdict: str) -> None:
        self.__verdict= verdict

    def getVerdict(self) -> str:
        return self.verdict
    
    def setPersonID(self, person_id: Person) -> None:
        self.__person_id= person_id

    def getPersonID(self) -> Person:
        return self.person_id

