from ModelM import Model 
from FusilladesM import Fusillade 
class Investigations(Model):

    def __init__(self):
        self.fusillade_id : Fusillade = None
    
    def setFusilladeID(self, _fusillade_id: Fusillade) -> None:
        self.fusillade_id = _fusillade_id

    def getFusilladeID(self) -> Fusillade:
        return self.fusillade_id


    def setAdvancement(self, _advancement: str) -> None:
        self.advancement = _advancement

    def getAdvancement(self) -> str:
        return self.advancement