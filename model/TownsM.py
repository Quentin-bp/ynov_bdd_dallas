from pydantic import BaseModel

from model.ModelM import Model 

class Towns(Model):

    def __init__(self):
        self.__name: str = ""
        self.__address_code: str = ""
        
    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setAddressCode(self, address_code: str) -> None:
        self.__address_code = address_code

    def getAddressCode(self) -> str:
        return self.__address_code


class TownModel(BaseModel):
    id : int = 0
    name: str = ""
    address_code: str = ""