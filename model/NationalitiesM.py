
class Nationality:
    """
    Classe qui représente le schema de la table Nationalities.
    """
    def __init__(self):
        self.__id: int = None
        self.__name: str =""

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

