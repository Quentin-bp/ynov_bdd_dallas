from dao.ModelDAO import ModelDAO
from model.InvestigationsPersonsM import InvestigationPoliceman
class InvestigationPolicemenDAO(ModelDAO):
    def __init__(self):
        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    ### CRUD

    def insertOne(self, objIns: InvestigationPoliceman)->int:
        query = '''INSERT INTO Investigation_Policemen (investigation_id, policeman_id) VALUES (%s, %s);'''
        values = (objIns.investigation_id, objIns.policeman_id)
        error = 'Erreur_InvestigationPolicemen.insertOne()'
        return super().operationTable(query, values, error) 

    def findAll(self)->list:
        pass

    def update(self,id,objUpdated)->int:
        pass

    def delete(self,id)->int:
        pass        