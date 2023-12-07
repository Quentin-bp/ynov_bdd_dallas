from ModelM import Model 

class Towns(Model):

    def __init__(self):
<<<<<<< HEAD
        self.__name: str = ""
        self.__adresse_code: str = ""
        
    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setAddressCode(self, address_code: str) -> None:
        self.__adresse_code = address_code

    def getAddressCode(self) -> str:
        return self.__adresse_code
=======
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
>>>>>>> 68d1df8aeaf75441f47f38b44bddd9deb6605ba2
