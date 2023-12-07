
class Model:
    def __init__(self):
        self.id: int = None

    def setID(self, _id: int) -> None:
        self.id = _id

    def getID(self) -> int:
        return self.id