from FusilladesM import ClassFusilladeM 

class ClassInvestigationM:

    def __init__(self):
        self.__id: int = None
        self.__fusillade : ClassFusilladeM = None
    
    def setFusilladeID(self, fusillade_id: ClassFusilladeM) -> None:
        self.__fusillade = fusillade_id

    def getFusilladeID(self) -> ClassFusilladeM:
        return self.__fusillade

    def setAdvancement(self, advancement: str) -> None:
        self.advancement = advancement

    def getAdvancement(self) -> str:
        return self.__advancement