from ModelM import Model 
from PersonsM import Person 
class Policemen(Model):

    def __init__(self):
        self.person_id : Person = None
        self.serial_numbers : str = ""   
        
    def setSerialNumbers(self, _serial_numbers: str) -> None:
        self.serial_numbers = _serial_numbers

    def getSerialNumbers(self) -> str:
        return self.serial_numbers
    
    def setPersonID(self, _person_id: Person) -> None:
        self.person_id = _person_id

    def getPersonID(self) -> Person:
        return self.person_id

