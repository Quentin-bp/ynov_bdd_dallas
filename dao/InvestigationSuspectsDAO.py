from dao.ModelDAO import ModelDAO

from model.InvestigationsPersonsM import InvestigationSuspect

from dao.SuspectsDAO import SuspectsDAO

from model.SuspectsM import Suspect

class InvestigationSuspectsDAO(ModelDAO):
    def __init__(self):
        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    ### CRUD

    def insertOne(self, objIns: InvestigationSuspect)->int:
        query = '''INSERT INTO Investigation_Suspects (investigation_id, suspect_id) VALUES (%s, %s);'''
        values = (objIns.investigation_id, objIns.suspect_id)
        error = 'Erreur_InvestigationSuspects.insertOne()'
        return super().operationTable(query, values, error) 

    def findAll(self)->list:
        pass

    def update(self,id,objUpdated)->int:
        pass

    def delete(self,id)->int:
        pass        

    def findAllSuspectsByInvestigation(self,investigation_id : int):
        try:
            query = '''SELECT * FROM Investigation_Suspects WHERE investigation_id LIKE %s'''
            self.cursor.execute(query,(investigation_id,) )
            res = self.cursor.fetchall()
            suspectsDao= SuspectsDAO()
            suspects = []

            if len(res) > 0:

                for r in res:
                    suspect : Suspect = suspectsDao.findById(r[1])
                    suspects.append(suspect)
                return suspects

            else:
                    return []
        except Exception as e:
            print(f"InvestigationSuspectsDAO.findAllByInvestigation() ::: {e}")