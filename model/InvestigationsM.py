from model.FusilladesM import Fusillade 
from pydantic import BaseModel

class Investigation:

    def __init__(self):
        self.__id: int = None
        self.__fusillade : Fusillade = None
        self.__advancement : str = ""

    def setID(self, id) -> None:
        self.__id = id

    def getID(self)->int:
        return self.__id
    
    def setFusilladeID(self, fusillade_id: Fusillade) -> None:
        self.__fusillade = fusillade_id

    def getFusilladeID(self) -> Fusillade:
        return self.__fusillade

    def setAdvancement(self, advancement: str) -> None:
        self.advancement = advancement

    def getAdvancement(self) -> str:
        return self.__advancement

class InvestigationModel(BaseModel):
    id : int
    fusillade_id : int
    advancement : str