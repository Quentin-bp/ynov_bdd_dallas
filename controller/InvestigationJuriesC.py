from dao.InvestigationJuriesDAO import InvestigationJuriesDAO
from dao.JuriesDAO import JuriesDAO
from dao.InvestigationsDAO import InvestigationsDAO

class InvestigationJuriesController:

    @staticmethod
    def insertOne(investigation_id: int, jury_id: int):

        dao = InvestigationJuriesDAO()
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
            print(f"Erreur_InvestigationJuriesController.insertOne() ::: {e}")
