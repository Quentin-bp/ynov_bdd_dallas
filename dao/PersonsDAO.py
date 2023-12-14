from dao.ModelDAO import ModelDAO
from dao.TownsDAO import TownsDAO
from dao.NationalitiesDAO import NationalitiesDAO
from model.PersonsM import Person, PersonModel

class PersonsDAO(ModelDAO):

    def __init__(self):
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()


    def findById(self, id: int)-> Person:
        try:
            query = """SELECT * FROM Persons WHERE id = %s;"""
            values = (id,)
            self.cursor.execute(query, values)
            res = self.cursor.fetchOne()

            townDao = TownsDAO()
            nationalityDao = NationalitiesDAO()

            if res:
                person = Person()
                person.setID(res[0])
                person.setLastName(res[1]) 
                person.setFirstName(res[2])
                person.setGenre(res[3])
                person.setStreetNumber(res[4]) 
                person.setStreetName(res[5])
                person.setAdditionalAddress(res[6])

                town = townDao.findById(res[7])
                nationality = nationalityDao.findById(res[8])

                person.setTownID(town) 
                person.setNationalityID(nationality)
                return person
            else:
                return None
        except Exception as e:
            print(f"Error_PersonDAO.findById() ::: {e}")


    def findAll(self)->'list[Person]':
        try:
            query="""SELECT * FROM Persons"""
            self.cursor.execute(query)
            res = self.sursor.fetchall()

            townDao = TownsDAO()
            nationalityDao = NationalitiesDAO()

            list_persons = []

            if len(res)>0:
                for r in res:
                    person = Person()
                    person.setID(r[0])
                    person.setLastName(r[1]) 
                    person.setFirstName(r[2])
                    person.setGenre(r[3])
                    person.setStreetNumber(r[4]) 
                    person.setStreetName(r[5])
                    person.setAdditionalAddress(r[6])

                    town = townDao.findById(r[7])
                    nationality = nationalityDao.findById(r[8])

                    person.setTown(town) 
                    person.setNationality(nationality)

                    list_persons.append(person)
                return list_persons
            else:
                return []

        except Exception as e:
            print(f"Error_PersonsDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Person)->int:
        query = """INSERT INTO Persons VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        values = (
                  ObjIns.getLastName(), 
                  ObjIns.getFirstName(),
                  ObjIns.getGenre(),
                  ObjIns.getStreetNumber(), 
                  ObjIns.getStreetName(),
                  ObjIns.getAdditionalAddress(),
                  ObjIns.getTown().getID(), 
                  ObjIns.getNationality().getID()
                 )
        error = "Erreur_PersonsDAO.insertOne()"
        return super().operationTable(query, values, error) 


    def update(self,id,objUpdated)->int:
        query = """UPDATE Persons SET last_name=%s, first_name=%s, genre=%s, street_number=%s, street_name=%s, additional_adress=%s, town_id=%s, nationality_id=%s WHERE id=%s"""
        values = (objUpdated.getLastName(), 
                  objUpdated.getFirstName(),
                  objUpdated.getGenre(),
                  objUpdated.getStreetNumber(), 
                  objUpdated.getStreetName(),
                  objUpdated.getAdditionalAddress(),
                  objUpdated.getTown().getID(), 
                  objUpdated.getNationalityID().getID(),
                  id
                 )
        error = "Erreur_PersonsDAO.update()"
        return super().operationTable(query, values, error) 


    def delete(self,id)->int:
        query = """DELETE FROM Persons WHERE id = %s;"""
        values = (id,)
        error = "Erreur_PersonsDAO.delete()"
        return super().operationTable(query, values, error)
