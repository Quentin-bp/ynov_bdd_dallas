from PersonsM import Person 

class Policeman:
    """
    Classe qui représente le schema de la table Policemen.
    """
    def __init__(self):
        self.__id: int = None
        self.__person_id : Person = None
        self.__serial_numbers : str = ""
        
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id
    
    def setSerialNumbers(self, serial_numbers: str) -> None:
        self.__serial_numbers = serial_numbers

    def getSerialNumbers(self) -> str:
        return self.__serial_numbers
    
    def setPersonID(self, person_id: Person) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> Person:
        return self.__person_id

