from dao.Investigation_PolicemenDAO import Investigation_PolicemenDAO
from dao.PolicemenDAO import PolicemenDAO
from dao.InvestigationsDAO import InvestigationsDAO

class Investigation_PolicemenController:

    @staticmethod
    def insertOne(investigation_id: int, policeman_id: int):

        dao = Investigation_PolicemenDAO()
        policemenDao = PolicemenDAO()
        investigationsDao = InvestigationsDAO()
        try:
            if (policemenDao.findById(policeman_id)==None):
                return 'This Policeman does not exist in database'
            elif (investigationsDao.findById(investigation_id)==None):
                return 'This investigation does not exist in database'
            else:
                res = dao.insertOne([investigation_id, policeman_id])
                if res == 0:
                    return 'ERROR'
                return "Association added"
        except Exception as e:
            print(f"Erreur_investigation_policemenController.insertOne() ::: {e}")
