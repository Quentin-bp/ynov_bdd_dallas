from ModelM import Model 
from PersonsM import Person 
class Juries(Model):

    def __init__(self):
        self.person_id : Person = None
    
    def setPersonID(self, _person_id: Person) -> None:
        self.person_id = _person_id

    def getPersonID(self) -> Person:
        return self.person_id

