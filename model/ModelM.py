
class Model:
    def __init__(self):
        self.__id: int = None

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self) -> int:
        return self.__id
