
class ClassTownM:
    """
    Classe qui représente le schema de la table Town.
    """
    def __init__(self):
        self.__id: int = None
        self.__name: str = ""
        self.__postal_code: str = ""
        
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setAddressCode(self, postal_code: str) -> None:
        self.__postal_code = postal_code

    def getAddressCode(self) -> str:
        return self.__postal_code
