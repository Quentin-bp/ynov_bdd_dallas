from dao.ModelDAO import ModelDAO
from model.InvestigationsPersonsM import InvestigationPoliceman
from dao.PolicemenDAO import PolicemenDAO
from model.PolicemenM import Policeman
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

    def findAllPolicemenByInvestigation(self,investigation_id : int):
        try:
            query = '''SELECT * FROM Investigation_Policemen WHERE investigation_id = %s'''
            self.cursor.execute(query,(investigation_id,) )
            res = self.cursor.fetchall()
            policemenDao= PolicemenDAO()
            policemen = []
            if len(res) > 0:

                for r in res:
                    suspect : Policeman = policemenDao.findById(r[1])
                    policemen.append(suspect)
                return policemen

            else:
                    return []
        except Exception as e:
            print(f"InvestigationSuspectsDAO.findAllPolicemenByInvestigation() ::: {e}")