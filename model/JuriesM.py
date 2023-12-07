from ModelM import Model 
from PersonsM import Person 
class Juries(Model):

    def __init__(self):
        self.__person_id : Person = None
    
    def setPersonID(self, person_id: Person) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> Person:
        return self.__person_id

