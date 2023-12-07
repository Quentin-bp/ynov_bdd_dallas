from ModelM import Model 
from PersonsM import Person 
class Policemen(Model):

    def __init__(self):
        self.__person_id : Person = None
        self.__serial_numbers : str = ""   
        
    def setSerialNumbers(self, serial_numbers: str) -> None:
        self.__serial_numbers = serial_numbers

    def getSerialNumbers(self) -> str:
        return self.__serial_numbers
    
    def setPersonID(self, person_id: Person) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> Person:
        return self.__person_id

