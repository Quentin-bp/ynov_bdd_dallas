from PersonsM import ClassPersonM 

class ClassSuspectM:
    """
    Classe qui représente le schema de la table Suspects.
    """
    def __init__(self):
        self.__id: int = None
        self.__person_id: ClassPersonM = None
        self.__verdict: str = ""   

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setVerdict(self, verdict: str) -> None:
        self.__verdict= verdict

    def getVerdict(self) -> str:
        return self.__verdict
    
    def setPersonID(self, person_id: ClassPersonM) -> None:
        self.__person_id= person_id

    def getPersonID(self) -> ClassPersonM:
        return self.__person_id

