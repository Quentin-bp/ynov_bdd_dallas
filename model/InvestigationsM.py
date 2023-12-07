from model.ModelM import Model 
from FusilladesM import Fusillade 
class Investigations(Model):

    def __init__(self):
        self.__fusillade : Fusillade = None
    
    def setFusilladeID(self, fusillade_id: Fusillade) -> None:
        self.__fusillade = fusillade_id

    def getFusilladeID(self) -> Fusillade:
        return self.__fusillade


    def setAdvancement(self, advancement: str) -> None:
        self.__advancement = advancement

    def getAdvancement(self) -> str:
        return self.__advancement