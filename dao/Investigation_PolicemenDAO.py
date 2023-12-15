from dao.ModelDAO import ModelDAO
from dao.ConnexionDAO import ConnexionBD

class Investigation_PolicemenDAO(ModelDAO):
    def __init__(self):
        params = ConnexionBD().getConnexion()
        #params = ModelDAO.connect_object
        self.cursor = params.cursor()

    ### CRUD

    def insertOne(self, objIns: 'list[int]')->int:
        query = '''INSERT INTO Investigation_Policemen (investigation_id, policeman_id) VALUES (%s, %s);'''
        values = (objIns[0], objIns[1])
        error = 'Erreur_Investigation_Policemen.insertOne()'
        return super().operationTable(query, values, error) 

    def findAll(self)->list:
        pass

    def update(self,id,objUpdated)->int:
        pass

    def delete(self,id)->int:
        pass        