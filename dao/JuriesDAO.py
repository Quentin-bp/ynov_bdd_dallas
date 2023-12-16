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
                        person = personDAO.findById(res[1])
                        jury = Jury()
                        jury.setID(r[0])
                        jury.setPerson(person)

                        juries.append(jury)
                    return juries

                else:
                    return []

            except Exception as e:
                print(f"Error_JuriesDAO.findAll() ::: {e}")

    def insertOne(self, objIns: Jury) -> int:

        try:
            query = '''INSERT INTO Juries (personId) VALUES (%s,);'''
            self.cursor.execute(query, (objIns.getPerson(),))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_JuriesDAO.insertOne() ::: {e}")
            self.cursor.connection.rollback()
            return 0

    def update(self, id, objUpdated: Jury) -> int:
        try:
            query = '''UPDATE Juries SET personId = %s WHERE id = %s;'''
            self.cursor.execute(query, (objUpdated.getPerson(), id))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_JuriesDAO.update() ::: {e}")
            self.cursor.connection.rollback()
            return 0

    def delete(self, id) -> int:
        try:
            query = '''DELETE FROM Juries WHERE id = %s;'''
            self.cursor.execute(query, (id,))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_JuriesDAO.delete() ::: {e}")
            self.cursor.connection.rollback()
            return 0