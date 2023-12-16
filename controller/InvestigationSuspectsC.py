from dao.InvestigationSuspectsDAO import InvestigationSuspectsDAO
from dao.SuspectsDAO import SuspectsDAO
from dao.InvestigationsDAO import InvestigationsDAO

class InvestigationSuspectsController:

    @staticmethod
    def insertOne(investigation_id: int, suspect_id: int):

        dao = InvestigationSuspectsDAO()
        suspectsDao = SuspectsDAO()
        investigationsDao = InvestigationsDAO()
        try:
            if (suspectsDao.findById(suspect_id)==None):
                return 'This Suspect does not exist in database'
            elif (investigationsDao.findById(investigation_id)==None):
                return 'This investigation does not exist in database'
            else:
                res = dao.insertOne([investigation_id, suspect_id])
                if res == 0:
                    return 'ERROR'
                return "Association added"
        except Exception as e:
            print(f"Erreur_InvestigationSuspectsController.insertOne() ::: {e}")
