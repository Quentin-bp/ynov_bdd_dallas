from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionBD

class ModelDAO(ABC):

    connect_objet = ConnexionBD().getConnexion()

    ### CRUD

    @abstractmethod
    def insertOne(self, objIns)->int:
        pass

    @abstractmethod
    def findAll(self)->list:
        pass

    @abstractmethod
    def update(self,id,objUpdated)->int:
        pass

    @abstractmethod
    def delete(self,id)->int:
        pass
    

    
    def operationTable(self, query : str, values : tuple, error: str = "Error_operationTable()"):
            try:
                self.cursor.execute(query, values,)   
                self.cursor.connection.commit()
                return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
            except Exception as e:
                print(f"{error} ::: {e}")
                self.cursor.connection.rollback()
                return 0
        