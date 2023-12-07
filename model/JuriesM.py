from PersonsM import ClassPersonM

class JuryM:
    """
    Classe qui représente le schema de la table Juries.
    """
    def __init__(self):
        self.__id : int = None
        self.__person_id : ClassPersonM = None
    
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setPersonID(self, person_id: ClassPersonM) -> None:
        self.__person_id = person_id

    def getPersonID(self) -> ClassPersonM:
        return self.__person_id

