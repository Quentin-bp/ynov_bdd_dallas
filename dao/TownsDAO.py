from dao.ModelDAO import ModelDAO
from model.TownsM import Town, TownModel  # Assurez-vous d'importer la classe BodyParts appropriée

class TownsDAO(ModelDAO):
    def __init__(self):

        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    def findById(self, id : int) -> Town:
        try:
            query = '''SELECT * FROM Towns WHERE id = %s;'''
            self.cursor.execute(query, (id,))
            res = self.cursor.fetchone()
            if res:
                town = Town()
                town.setID(res[0])
                town.setName(res[1])
                town.setPostalCode(res[2])
                return town
            else:
                return None
        except Exception as e:
            print(f"Error_TownsDAO.findById() ::: {e}")

        
    def findAll(self) -> 'list[Town]':
            try:
                query = '''SELECT * FROM Towns'''
                self.cursor.execute(query)
                res = self.cursor.fetchall()

                towns = []
                
                if len(res)>0:

                    for r in res:
                        town = Town()
                        town.setID(r[0])
                        town.setName(r[1])
                        town.setPostalCode(r[2])

                        towns.append(town)

                    return towns

                else:

                    return []

            except Exception as e:
                print(f"Error_TownsDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Town) -> int:
        query = '''INSERT INTO Towns (name, postal_code) VALUES (%s, %s);'''
        values = (objIns.getName(),objIns.getPostalCode())
        error = "Erreur_TownsDAO.insertOne()"
        return super().operationTable(query, values,error)
        

    def update(self, id , objUpdated : Town)->int:
        query = '''UPDATE Towns SET name = %s,postal_code = %s WHERE id = %s;'''
        values =  (objUpdated.getName(), objUpdated.getPostalCode(),id)
        error = "Erreur_TownsDAO.update()"
        return super().operationTable(query, values,error)

        
    def delete(self,id)->int:
        query = '''DELETE FROM Towns WHERE id = %s;'''
        values =  (id,)
        error = "Erreur_TownsDAO.delete()"
        return super().operationTable(query, values,error)