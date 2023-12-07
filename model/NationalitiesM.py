from ModelM import Model 
class Nationalities(Model):

    def __init__(self):
        self.name: str = ""

    def setName(self, _name: str) -> None:
        self.name = _name

    def getName(self) -> str:
        return self.name

