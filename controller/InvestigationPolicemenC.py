from dao.InvestigationPolicemenDAO import InvestigationPolicemenDAO
from dao.PolicemenDAO import PolicemenDAO
from dao.InvestigationsDAO import InvestigationsDAO
from model.InvestigationsPersonsM import InvestigationPoliceman
class InvestigationPolicemenController:

    @staticmethod
    def insertOne(link : InvestigationPoliceman):

        dao = InvestigationPolicemenDAO()
        policemenDao = PolicemenDAO()
        investigationsDao = InvestigationsDAO()
        try:
            if (policemenDao.findById(link.policeman_id)==None):
                return 'This Policeman does not exist in database'
            elif (investigationsDao.findById(link.investigation_id)==None):
                return 'This investigation does not exist in database'
            else:
                res = dao.insertOne(link)
                if res == 0:
                    return 'ERROR'
                return "Association added"
        except Exception as e:
            print(f"Erreur_InvestigationPolicemenController.insertOne() ::: {e}")
