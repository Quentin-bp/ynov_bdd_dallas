from ModelM import Model 
class Nationalities(Model):

    def __init__(self):
<<<<<<< HEAD
        self.__name: str = ""

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name
=======
        self.name: str = ""

    def setName(self, _name: str) -> None:
        self.name = _name

    def getName(self) -> str:
        return self.name
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2

