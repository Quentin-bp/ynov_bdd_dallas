from TownsM import ClassTownM
from NationalitiesM import ClassNationalityM


class ClassPersonM:
    """
    Classe qui représente le schema de la table Persons.
    """
    def __init__(self):
        self.__id: int = None
        self.__firstname: str = ""
        self.__lastname: str = ""
        self.__genre : int = None
        self.__numero_rue : str = "" # exple 1 bis
        self.__nom_rue: str = ""
        self.__complement_adress: str = ""
        self.__town_id : ClassTownM = None
        self.__nationality_id : ClassNationalityM = None

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setFirstName(self, firstname: str) -> None:
        self.__firstname = firstname

    def getFirstName(self) -> str:
        return self.__firstname

    def setLastName(self, lastname: str) -> None:
        self.__lastname = lastname

    def getLastName(self) -> str:
        return self.__lastname
  
    def setGenre(self, genre: str) -> None:
        self.__genre = genre

    def getGenre(self) -> str:
        return self.__genre
    
    def setNumeroRue(self, numero_rue: str) -> None:
        self.__numero_rue = numero_rue

    def getNumeroRue(self) -> str:
        return self.__numero_rue

    def setNomRue(self, nom_rue: str) -> None:
        self.__nom_rue = nom_rue

    def getNomRue(self) -> str:
        return self.__nom_rue

    def setComplementAddress(self, complement_address: str) -> None:
        self.__complement_adress = complement_address

    def getComplementAddress(self) -> str:
        return self.__complement_adress
    
    def setTownID(self, town_id: ClassTownM) -> None:
        self.__town_id = town_id

    def getTownID(self) -> ClassTownM:
        return self.__town_id
    
    def setNationalityID(self, nationality_id: ClassNationalityM) -> None:
        self.__nationality_id = nationality_id

    def getNationalityID(self) -> ClassNationalityM:
        return self.__nationality_id
