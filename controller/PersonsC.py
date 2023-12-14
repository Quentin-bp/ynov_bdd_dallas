from dao.PersonsDAO import PersonsDAO
from model.PersonsM import Person, PersonModel
from dao.TownsDAO import TownsDAO
from dao.NationalitiesDAO import NationalitiesDAO


class PersonsController:

    @staticmethod
    def findById(id):
        try:
            dao = PersonsDAO()
            print(id)
            person: Person = dao.findById(id)

            if person==None :
                return "Person not found"

            return person

        except Exception as e:
            print(f'Erreur_PersonsC.findById() ::: {e}')

        return None
    
    @staticmethod
    def findAll():
        try:
            dao = PersonsDAO()
            list_persons: list[Person] = dao.findAll()

            if len(list_persons)==0 :
                return "There is no person in database"

            return list_persons

        except Exception as e:
            print(f'Erreur_PersonsC.findAll() ::: {e}')

        return None

    @staticmethod
    def insertOne(person : PersonModel):

        dao = PersonsDAO()
        daoTown = TownsDAO()
        daoNationality = NationalitiesDAO()
        try:
            town = daoTown.findById(person.town_id)
            if (town == None):
                return 'This Town id is not founded/does not exists in database'

            nationality = daoTown.findById(person.nationality_id)
            if (nationality == None):
                return 'This Nationality id is not founded/does not exists in database'    

            newPerson = Person()

            newPerson.setFirstName(person.firstname)
            newPerson.setLastName(person.lastname)
            newPerson.setGenre(person.genre)
            newPerson.setStreetNumber(person.street_number)
            newPerson.setStreetName(person.street_name)
            newPerson.setAdditionnalAddress(person.additional_address)
            newPerson.setTown(town)
            newPerson.setNationality(nationality)

            res: int = dao.insertOne(newPerson)

            if res==0:
                return "ERROR"

            return "Person Added"

        except Exception as e:
            print(f'Erreur_PersonsC.insertOne() ::: {e}')

        return None

    @staticmethod
    def update(person : PersonModel):

        dao = PersonsDAO()
        daoTown = TownsDAO()
        daoNationality = NationalitiesDAO()
        try:
            town = daoTown.findById(person.town_id)
            if (town == None):
                return 'This Town id is not founded/does not exists in database'

            nationality = daoTown.findById(person.nationality_id)
            if (nationality == None):
                return 'This Nationality id is not founded/does not exists in database'    

            updatedPerson = Person()

            updatedPerson.setID(person.id)
            updatedPerson.setFirstName(person.firstname)
            updatedPerson.setLastName(person.lastname)
            updatedPerson.setGenre(person.genre)
            updatedPerson.setStreetNumber(person.street_number)
            updatedPerson.setStreetName(person.street_name)
            updatedPerson.setAdditionnalAddress(person.additional_address)

            newPerson.setTown(town)
            newPerson.setNationality(nationality)

            res: int = dao.update(person.id, updatedPerson)

            if res==0:
                return "ERROR"

            return "Person Updated"

        except Exception as e:
            print(f'Erreur_PersonsC.update() ::: {e}')

        return None
    
    @staticmethod
    def delete(id):
        try:
            dao = PersonsDAO()
            res: int = dao.delete(id)
            if res==0 :
                return "ERROR"
            return "Person deleted"
        except Exception as e:
            print(f'Erreur_PersonC.delete() ::: {e}')
            return None