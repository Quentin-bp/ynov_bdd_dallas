from dao.ModelDAO import ModelDAO
from model.TownsM import Towns, TownModel  # Assurez-vous d'importer la classe BodyParts appropriée

class TownsDAO(ModelDAO):
    def __init__(self):

        params = ModelDAO.connect_objet
        self.cursor = params.cursor() 
        
    def findAll(self) -> list[Towns]:
            try:
                query = '''SELECT * FROM Towns'''
                self.cursor.execute(query)
                res = self.cursor.fetchall()

                towns = []
                
                if len(res)>0:

                    for r in res:
                        town = Towns()

                        town.setName(r[0])
                        town.setAddressCode(r[1])

                        towns.append(town)

                    return towns

                else:

                    return []

            except Exception as e:
                print(f"Error_TownsDAO.findAll() ::: {e}")


    def insertOne(self, objIns: Towns) -> int:
        '''
        Insère un objet dans la table BodyParts.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO Towns (name, address_code) VALUES (%s, %s);'''
            self.cursor.execute(query, (objIns.getName(),objIns.getAddressCode(),))
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_TownsDAO.insertOne() ::: {e}")
            self.cursor.connection.rollback()
            return 0