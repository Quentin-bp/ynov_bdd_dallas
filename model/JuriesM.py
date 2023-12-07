from ModelM import Model 
from PersonsM import PersonM

class JuryM(Model):

    def __init__(self):
        self.__person_id : PersonM = None
    
    def setPersonID(self, person_id: PersonM) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> PersonM:
        return self.__person_id

