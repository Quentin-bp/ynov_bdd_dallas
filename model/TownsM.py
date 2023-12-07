from ModelM import Model 

class Towns(Model):

    def __init__(self):
        self.__name: str = ""
        self.postal_code: str = ""
        
    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setAddressCode(self, address_code: str) -> None:
        self.postal_code = address_code

    def getAddressCode(self) -> str:
        return self.postal_code
