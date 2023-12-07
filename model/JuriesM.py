from ModelM import Model 
from PersonsM import Person 
class Juries(Model):

    def __init__(self):
<<<<<<< HEAD
        self.__person_id : Person = None
    
    def setPersonID(self, person_id: Person) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> Person:
        return self.__person_id
=======
        self.person_id : Person = None
    
    def setPersonID(self, _person_id: Person) -> None:
        self.person_id = _person_id

    def getPersonID(self) -> Person:
        return self.person_id
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2

