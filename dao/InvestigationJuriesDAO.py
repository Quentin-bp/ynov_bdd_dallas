from dao.ModelDAO import ModelDAO

from dao.JuriesDAO import JuriesDAO
from model.JuriesM import Jury

class InvestigationJuriesDAO(ModelDAO):
    def __init__(self):
        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    ### CRUD

    def insertOne(self, objIns: list[int])->int:
        query = '''INSERT INTO InvestigationJuries (investigation_id, jury_id) VALUES (%s, %s);'''
        values = (objIns[0], objIns[1])
        error = 'Erreur_InvestigationJuries.insertOne()'
        return super().operationTable(query, values, error) 

    def findAll(self)->list:
        pass

    def update(self,id,objUpdated)->int:
        pass

    def delete(self,id)->int:
        pass        

    def findAllJuriesByInvestigation(self,investigation_id : int):
        try:
            query = '''SELECT * FROM Investigation_Juries WHERE investigation_id = %s'''
            self.cursor.execute(query,(investigation_id,) )
            res = self.cursor.fetchall()
            juriesDao= JuriesDAO()
            juries = []
            if len(res) > 0:

                for r in res:
                    jury : Jury = juriesDao.findById(r[1])
                    juries.append(jury)
                return juries

            else:
                    return []
        except Exception as e:
            print(f"InvestigationSuspectsDAO.findAllJuriesByInvestigation() ::: {e}")