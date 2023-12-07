from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionBD

class ModelDAO(ABC):

    connect_objet = ConnexionBD().getConnexion()

    ### CRUD

    # INSERT

    @abstractmethod
    def insertOne(self, objIns)->int:
        pass

    # SELECT
    @abstractmethod
    def findAll(self)->list:
        pass

        # SELECT
    @abstractmethod
    def update(self,id,objIns)->int:
        pass

    

    # DELETE : faire une recherche plein texte