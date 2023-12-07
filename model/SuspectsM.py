from ModelM import Model 
from PersonsM import Person 
class Suspects(Model):

    def __init__(self):
        self.person_id : Person = None
        self.verdict : str = ""   
        
    def setVerdict(self, _verdict: str) -> None:
        self.verdict = _verdict

    def getVerdict(self) -> str:
        return self.verdict
    
    def setPersonID(self, _person_id: Person) -> None:
        self.person_id = _person_id

    def getPersonID(self) -> Person:
        return self.person_id

