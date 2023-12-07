from ModelM import Model 
from PersonsM import Person 
class Suspects(Model):

    def __init__(self):
<<<<<<< HEAD
        self.__person_id: Person = None
        self.__verdict: str = ""   
        
    def setVerdict(self, verdict: str) -> None:
        self.__verdict= verdict
=======
        self.person_id : Person = None
        self.verdict : str = ""   
        
    def setVerdict(self, _verdict: str) -> None:
        self.verdict = _verdict
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2

    def getVerdict(self) -> str:
        return self.verdict
    
<<<<<<< HEAD
    def setPersonID(self, person_id: Person) -> None:
        self.__person_id= person_id
=======
    def setPersonID(self, _person_id: Person) -> None:
        self.person_id = _person_id
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2

    def getPersonID(self) -> Person:
        return self.person_id

