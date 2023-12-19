from dao.ModelDAO import ModelDAO
from model.JuriesM import Jury, JuryModel
from dao.PersonsDAO import PersonsDAO

class JuriesDAO(ModelDAO):
    def __init__(self):

        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    def findById(self, id: int) -> Jury:
            try:
                query = '''SELECT * FROM Juries WHERE id = %s;'''
                personDAO = PersonsDAO()
                self.cursor.execute(query, (id,))
                res = self.cursor.fetchone()
                if res:
                    person = personDAO.findById(res[1])
                    jury = Jury()
                    jury.setID(res[0])
                    jury.setPerson(person)
                    return jury
                else:
                    return None
            except Exception as e:
                print(f"Error_JuriesDAO.findById() ::: {e}")

    def findAll(self) -> list[Jury]:
            try:
                query = '''SELECT * FROM Juries'''
                personDAO = PersonsDAO()
                self.cursor.execute(query)
                res = self.cursor.fetchall()

                juries = []
                if len(res) > 0:

                    for r in res:
                        person = personDAO.findById(r[1])
                        jury = Jury()
                        jury.setID(r[0])
             
                        jury.setPerson(person)

                        juries.append(jury)
                    print(juries)
                    return juries

                else:
                    return []

            except Exception as e:
                print(f"Error_JuriesDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Jury)->int:
        query = '''INSERT INTO Juries (person_id) VALUES (%s)'''
        values = (objIns.getPerson().getID(),)
        error = "Erreur_JuriesDAO.insertOne()"

        return super().operationTable(query, values, error) 


    def update(self,id : int, objUpdated : Jury)->int:
        query = """UPDATE Juries SET person_id = %s WHERE id=%s"""
        values = (objUpdated.getPerson().getID(),id)
        error = "Erreur_JuriesDAO.update()"
        return super().operationTable(query, values, error) 


    def delete(self,id : int)->int:
        query = """DELETE FROM Juries WHERE id = %s"""
        values = (id,)
        error = "Erreur_JuriesDAO.delete()"
        return super().operationTable(query, values, error)