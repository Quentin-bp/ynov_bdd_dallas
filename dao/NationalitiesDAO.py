from dao.ModelDAO import ModelDAO
from model.NationalitiesM import Nationality


class NationalitiesDAO(ModelDAO):
    def __init__(self):

        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    def findById(self, id: int) -> Nationality:
        try:
            query = '''SELECT * FROM Nationalities WHERE id = %s ;'''

            self.cursor.execute(query, (id,))
            res = self.cursor.fetchone()
            if res:
                nationality = Nationality()
                nationality.setID(res[0])
                nationality.setName(res[1])
                return nationality
            else:
                return None
        except Exception as e:
            print(f"Error_NationalitiesDAO.findById() ::: {e}")

    def findAll(self) -> list:
        try:
            query = '''SELECT * FROM  Nationalities;'''

            self.cursor.execute(query)
            res = self.cursor.fetchall()

            nationalities = []

            if len(res) > 0:

                for r in res:
                    print(r)
                    nationality = Nationality()
                    nationality.setName(r[1])
                    nationality.setID(r[0])
                    nationalities.append(nationality)
                return nationalities
            else:
                return []
        except Exception as e:
            print(f"Error_NationalitiesDAO.findAll() ::: {e}")

    def insertOne(self, objIns: Nationality)->int:
        query = '''INSERT INTO Nationalities (name) VALUES (%s)'''
        values = (objIns.getName(),)
        error = "Erreur_NationalitiesDAO.insertOne()"

        return super().operationTable(query, values, error) 


    def update(self,id,objUpdated)->int:
        query = """UPDATE Nationalities SET name = %s WHERE id=%s"""
        values = (objUpdated.getName(),id)
        error = "Erreur_NationalitiesDAO.update()"
        return super().operationTable(query, values, error) 


    def delete(self,id)->int:
        query = """DELETE FROM Nationalities WHERE id = %s"""
        values = (id,)
        error = "Erreur_Nationalities.delete()"
        return super().operationTable(query, values, error)