from dao.ModelDAO import ModelDAO
from dao.PersonsDAO import PersonsDAO
from model.SuspectsM import Suspect, SuspectModel


class SuspectsDAO(ModelDAO):
    def __init__(self):
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()


    def findById(self, id: int)-> Suspect:
        try:
            query = """SELECT * FROM Suspects WHERE id = %s;"""
            values = (id,)
            self.cursor.execute(query, values)
            res = self.cursor.fetchOne()

            personDao = PersonsDAO()

            if res:
                Suspect = Suspect()

                Suspect.setID(res[0])

                person = personDao.findById(res[1])
                Suspect.setPerson(person)

                Suspect.setVerdict(res[2])

                return Suspect
            else:
                return None
        except Exception as e:
            print(f"Error_SuspectsDAO.findById() ::: {e}")


    def findAll(self)->'list[Person]':
        try:
            query="""SELECT * FROM Suspects"""
            self.cursor.execute(query)
            res = self.sursor.fetchall()

            personDao = personsDAO()

            list_suspects = []

            if len(res)>0:
                for r in res:
                    suspect = Suspect()

                    suspect.setID(r[0])

                    person = personDao.findByID(res[1])
                    suspect.setPerson(person)

                    suspect.setVerdict(r[2]) 

                    list_suspects.append(suspect)
                return list_suspects
            else:
                return []

        except Exception as e:
            print(f"Error_SuspectsDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Suspect)->int:
        query = """INSERT INTO Suspects VALUES (%s, %s);"""
        values = (ObjIns.getPerson().getID(), 
                  ObjIns.getVerdict()
                 )
        error = "Erreur_SuspectsDAO.insertOne()"
        return super().operationTable(query, values, error) 


    def update(self,id,objUpdated)->int:
        query="""UPDATE Suspects SET person_id=%s, serial_numbers=% WHERE id=%s"""
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
