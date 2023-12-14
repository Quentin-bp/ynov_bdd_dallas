from dao.ModelDAO import ModelDAO
from model.NationalitiesM import Nationality
from dao.ModelDAO import ModelDAO


class NationalitiesDAO(ModelDAO):
    def __init__(self):

        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    def findById(self, id: int) -> Nationality:
        try:
            query = '''SELECT * FROM Nationality WHERE id = %s ;'''

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

    def findAll(self) -> 'list[Nationality]':
        try:
            query = '''SELECT * FROM Nationality'''

            self.cursor.execute(query)
            res = self.cursor.fetchall()

            nationalities = []

            if len(res) > 0:

                for r in res:
                    nationality = Nationality()
                    nationality.setID(r[0])
                    nationality.setName(r[1])

                    nationalities.append(nationality)
                return nationalities
            else:
                return []
        except Exception as e:
            print(f"Error_NationalitiesDAO.findAll() ::: {e}")

    def insertOne(self, objIns: Nationality) -> int:

        try:
            query = '''INSERT INTO Nationality (name) VALUES (%s,);'''
            self.cursor.execute(query, (objIns.getName(),))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_NationaltiesDAO.insertOne() ::: {e}")
            self.cursor.connection.rollback()
            return 0

    def update(self, id, objUpdated: Nationality) -> int:
        try:
            query = '''UPDATE Nationality SET name = %s WHERE id = %s;'''
            self.cursor.execute(query, (objUpdated.getName(), id))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_NationalitiesDAO.update() ::: {e}")
            self.cursor.connection.rollback()
            return 0

    def delete(self, id) -> int:
        try:
            query = '''DELETE FROM Nationality WHERE id = %s;'''
            self.cursor.execute(query, (id,))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_Nationalities.delete() ::: {e}")
            self.cursor.connection.rollback()
            return 0