from dao.InvestigationSuspectsDAO import InvestigationSuspectsDAO
from dao.SuspectsDAO import SuspectsDAO
from dao.InvestigationsDAO import InvestigationsDAO
from model.InvestigationsPersonsM import InvestigationSuspect
class InvestigationSuspectsController:

    @staticmethod
    def insertOne(link : InvestigationSuspect):

        dao = InvestigationSuspectsDAO()
        suspectsDao = SuspectsDAO()
        investigationsDao = InvestigationsDAO()
        try:
            if (suspectsDao.findById(link.suspect_id)==None):
                return 'This Suspect does not exist in database'
            elif (investigationsDao.findById(link.investigation_id)==None):
                return 'This investigation does not exist in database'
            else:
                res = dao.insertOne(link)
                if res == 0:
                    return 'ERROR'
                return "Association added"
        except Exception as e:
            print(f"Erreur_InvestigationSuspectsController.insertOne() ::: {e}")
