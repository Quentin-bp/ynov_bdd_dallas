from dao.Investigation_JuriesDAO import Investigation_JuriesDAO
from dao.JuriesDAO import JuriesDAO
from dao.InvestigationsDAO import InvestigationsDAO

class Investigation_JuriesController:

    @staticmethod
    def insertOne(investigation_id: int, jury_id: int):

        dao = Investigation_JuriesDAO()
        juriesDao = JuriesDAO()
        investigationsDao = InvestigationsDAO()
        try:
            if (juriesDao.findById(jury_id)==None):
                return 'This Jury does not exist in database'
            elif (investigationsDao.findById(investigation_id)==None):
                return 'This investigation does not exist in database'
            else:
                res = dao.insertOne([investigation_id, jury_id])
                if res == 0:
                    return 'ERROR'
                return "Association added"
        except Exception as e:
            print(f"Erreur_investigation_juriesController.insertOne() ::: {e}")
