from TownsM import Town 

class Fusillade:

    def __init__(self):
        self.__id : int = None
        self.__street_number : str = "" # exple 1 bis
        self.__street_name: str = ""
        self.__additional_address: str = ""
        self.__description : str = ""
        self.__date : str = ""
        self.__town_id : Town = None

    def setID(self, id: int) -> None:
        self.__id = id

    def getID(self, id: int) -> int:
        return self.__id

    def setStreetNumber(self, street_number: str) -> None:
        self.__street_number = street_number

    def getStreetNumber(self) -> str:
        return self.__street_number

    def setStreetName(self, street_name: str) -> None:
        self.__street_name = street_name

    def getStreetName(self) -> str:
        return self.__street_name

    def setAdditionalAddress(self, additional_address: str) -> None:
        self.__additional_address = additional_address

    def getAdditionalAddress(self) -> str:
        return self.__additional_address
    
    def setTownID(self, town_id: Town) -> None:
        self.__town_id = town_id

    def getTownID(self) -> Town:
        return self.__town_id
    
    def setDate(self, date: str) -> None:
        self.__date = date

    def getDate(self) -> str:
        return self.__date
    
    def setDescription(self, description: str) -> None:
        self.__description = description

    def getDescription(self) -> str:
        return self.__description
