from model.ModelM import Model 
class Nationalities(Model):

    def __init__(self):
        self.__name: str = ""

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

