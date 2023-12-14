from dao.ModelDAO import ModelDAO
from dao.PersonsDAO import PersonsDAO
from model.PolicemenM import Policeman, PolicemanModel


class PolicemenDAO(ModelDAO):
    def __init__(self):
        
        #params = ModelDAO.connect_object
        #params = ConnexionBD().getConnexion()
        params = ModelDAO.connect_objet
        self.cursor = params.cursor()


    def findById(self, id: int)-> Policeman:
        try:
            query = """SELECT * FROM Policemen WHERE id = %s;"""
            values = (id,)
            self.cursor.execute(query, values)
            res = self.cursor.fetchone()

            personDao = PersonsDAO()

            if res:
                policeman = Policeman()

                policeman.setID(res[0])

                person = personDao.findById(res[1])
                policeman.setPerson(person)

                policeman.setSerialNumbers(res[2])

                return policeman
            else:
                return None
        except Exception as e:
            print(f"Error_PolicemenDAO.findById() ::: {e}")


    def findAll(self)->'list[Policeman]':
        try:
            query="""SELECT * FROM Policemen"""
            self.cursor.execute(query)
            res = self.cursor.fetchall()

            personDao = PersonsDAO()
            list_policemen = []

            if len(res)>0:
                for r in res:
                    policeman = Policeman()

                    policeman.setID(r[0])

                    person = personDao.findById(r[1])
                    policeman.setPerson(person)

                    policeman.setSerialNumbers(r[2]) 
                    list_policemen.append(policeman)
                return list_policemen
            else:
                return []

        except Exception as e:
            print(f"Error_PolicemenDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Policeman)->int:
        query = """INSERT INTO Policemen (person_id, serial_numbers) VALUES (%s, %s);"""
        values = (objIns.getPerson().getID(), 
                  objIns.getSerialNumbers()
                 )
        error = "Erreur_PolicemenDAO.insertOne()"
        return super().operationTable(query, values, error) 


    def update(self,id,objUpdated)->int:
        query = """UPDATE Policemen SET person_id=%s, serial_numbers=% WHERE id=%s"""
        values = (objUpdated.getPerson().getID(),
                  objUpdated.getSerialNumbers(),
                  id
                 )
        error = "Erreur_PolicemenDAO.update()"
        return super().operationTable(query, values, error) 


    def delete(self,id)->int:
        query = """DELETE FROM Policemen WHERE id = %s;"""
        values = (id,)
        error = "Erreur_PolicemenDAO.delete()"
        return super().operationTable(query, values, error)
