from model.FusilladesM import Fusillade 
from pydantic import BaseModel
from enum import Enum

class Status(Enum):
    Without_follow_up = "without_follow_up"
    Ongoing = "ongoing"
    Classified = "classified"

class Investigation:

    def __init__(self):
        self.__id: int = None
        self.__fusillade : Fusillade = None
        self.__advancement : str = "",
        self.__status : Status = Status.Ongoing,

    def setID(self, id) -> None:
        self.__id = id

    def getID(self)->int:
        return self.__id
    
    def setFusillade(self, fusillade: Fusillade) -> None:
        self.__fusillade = fusillade

    def getFusillade(self) -> Fusillade:
        return self.__fusillade

    def setAdvancement(self, advancement: str) -> None:
        self.__advancement = advancement

    def getAdvancement(self) -> str:
        return self.__advancement
    
    def getStatus(self) -> Status:
        return self.__status
    
    def setStatus(self, status: Status) -> None:
        self.__status = status
    
    def setStatus(self, status: str) -> None:
        try:
            self.__status = Status[status.capitalize()]
        except KeyError:
            raise ValueError("The status "  + status + " is not a valid status")


class InvestigationModel(BaseModel):
    fusillade_id : int
    advancement : str
    status : str = ""