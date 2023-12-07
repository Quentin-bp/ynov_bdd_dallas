from ModelM import Model 
from FusilladesM import Fusillade 
class Investigations(Model):

    def __init__(self):
<<<<<<< HEAD
        self.__fusillade : Fusillade = None
    
    def setFusilladeID(self, fusillade_id: Fusillade) -> None:
        self.__fusillade = fusillade_id

    def getFusilladeID(self) -> Fusillade:
        return self.__fusillade


    def setAdvancement(self, advancement: str) -> None:
        self.advancement = advancement
=======
        self.fusillade_id : Fusillade = None
    
    def setFusilladeID(self, _fusillade_id: Fusillade) -> None:
        self.fusillade_id = _fusillade_id

    def getFusilladeID(self) -> Fusillade:
        return self.fusillade_id


    def setAdvancement(self, _advancement: str) -> None:
        self.advancement = _advancement
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2

    def getAdvancement(self) -> str:
        return self.advancement