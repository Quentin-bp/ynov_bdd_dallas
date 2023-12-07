from TownsM import ClassTownM 

class ClassFusilladeM:

    def __init__(self):
        self.__id : int = None
        self.__numero_rue : str = "" # exple 1 bis
        self.__nom_rue: str = ""
        self.__complement_address: str = ""
        self.__town_id : ClassTownM = None
        self.__description : str = ""
        self.__date : str = ""
       
    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setNumeroRue(self, numero_rue: str) -> None:
        self.__numero_rue = numero_rue

    def getNumeroRue(self) -> str:
        return self.__numero_rue

    def setNomRue(self, nom_rue: str) -> None:
        self.__nom_rue = nom_rue

    def getNomRue(self) -> str:
        return self.__nom_rue

    def setComplementAddress(self, complement_address: str) -> None:
        self.__complement_address = complement_address

    def getComplementAddress(self) -> str:
        return self.__complement_address
    
    def setTownID(self, town_id: ClassTownM) -> None:
        self.__town_id = town_id

    def getTownID(self) -> ClassTownM:
        return self.__town_id
    
    def setDate(self, date: str) -> None:
        self.__date = date

    def getDate(self) -> str:
        return self.__date
    
    def setDescription(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description
