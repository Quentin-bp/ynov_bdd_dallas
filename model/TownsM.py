from ModelM import Model 

class Towns(Model):

    def __init__(self):
        self.name: str = ""
        self.address_code: str = ""
        
    def setName(self, _name: str) -> None:
        self.name = _name

    def getName(self) -> str:
        return self.name

    def setAddressCode(self, _address_code: str) -> None:
        self.address_code = _address_code

    def getAddressCode(self) -> str:
        return self.address_code