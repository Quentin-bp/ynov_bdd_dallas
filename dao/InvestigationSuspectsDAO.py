from dao.ModelDAO import ModelDAO

class InvestigationSuspectsDAO(ModelDAO):
    def __init__(self):
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    ### CRUD

    def insertOne(self, objIns: list[int])->int:
        query = '''INSERT INTO InvestigationSuspects (investigation_id, suspect_id) VALUES (%s, %s);'''
        values = (objIns[0], objIns[1])
        error = 'Erreur_InvestigationSuspects.insertOne()'
        return super().operationTable(query, values, error) 

    def findAll(self)->list:
        pass

    def update(self,id,objUpdated)->int:
        pass

    def delete(self,id)->int:
        pass        