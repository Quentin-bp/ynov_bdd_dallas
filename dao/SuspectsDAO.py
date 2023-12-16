from dao.ModelDAO import ModelDAO
from dao.PersonsDAO import PersonsDAO
from model.SuspectsM import Suspect, SuspectModel
from model.PersonsM import Person
from dao.ConnexionDAO import ConnexionBD

class SuspectsDAO(ModelDAO):
    def __init__(self):

        #params = ModelDAO.connect_object
        params = ConnexionBD().getConnexion()
        self.cursor = params.cursor()


    def findById(self, id: int)-> Suspect:
        try:
            query = """SELECT * FROM Suspects WHERE id = %s;"""
            values = (id,)
            self.cursor.execute(query, values)
            res = self.cursor.fetchone()

            personDao = PersonsDAO()

            if res:
                suspect = Suspect()

                suspect.setID(res[0])

                person = personDao.findById(res[1])
                suspect.setPerson(person)

                suspect.setVerdict(res[2])

                return suspect
            else:
                return None
        except Exception as e:
            print(f"Error_SuspectsDAO.findById() ::: {e}")


    def findAll(self)->list[Suspect]:
        try:
            query="""SELECT * FROM Suspects"""
            self.cursor.execute(query)
            res = self.cursor.fetchall()

            personDao = PersonsDAO()

            list_suspects = []

            if len(res)>0:
                for r in res:
                    suspect = Suspect()

                    suspect.setID(r[0])

                    person = personDao.findById(r[1])
                    suspect.setPerson(person)

                    suspect.setVerdict(r[2]) 

                    list_suspects.append(suspect)
                return list_suspects
            else:
                return []

        except Exception as e:
            print(f"Error_SuspectsDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Suspect)->int:
        query = """INSERT INTO Suspects (person_id, verdict) VALUES (%s, %s);"""
        values = (objIns.getPerson().getID(), 
                  objIns.getVerdict()
                 )
        error = "Erreur_SuspectsDAO.insertOne()"
        return super().operationTable(query, values, error) 


    def update(self,id,objUpdated)->int:
        query="""UPDATE Suspects SET person_id=%s, verdict=% WHERE id=%s"""
        values = (objUpdated.getPerson().getID(),
                  objUpdated.getVerdict(),
                  id
                 )
        error = "Erreur_SuspectsDAO.update()"
        return super().operationTable(query, values, error) 


    def delete(self,id)->int:
        query = """DELETE FROM Suspects WHERE id = %s;"""
        values = (id,)
        error = "Erreur_SuspectsDAO.delete()"
        return super().operationTable(query, values, error)
