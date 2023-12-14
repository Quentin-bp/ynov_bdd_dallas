from dao.ModelDAO import ModelDAO
from dao.TownsDAO import TownsDAO
from model.FusilladesM import Fusillade #, FusilladeModel  # Assurez-vous d'importer la classe BodyParts appropriée

class FusilladesDAO(ModelDAO):
    def __init__(self):

        params = ModelDAO.connect_objet
        self.cursor = params.cursor() 


    def findById(self, id : int) -> Fusillade:
        try:
            query = '''SELECT * FROM Fusillades WHERE id = %s;'''
            townDao = TownsDAO()
            self.cursor.execute(query, (id,))
            res = self.cursor.fetchone()
            if res:
                town = townDao.findById(res[6])
                fusillade = Fusillade()
                fusillade.setID(res[0])
                fusillade.setStreetNumber(res[1])
                fusillade.setStreetName(res[2])
                fusillade.setAdditionalAddress(res[3])
                fusillade.setDate(res[4])
                fusillade.setDescription(res[5])
                fusillade.setTown(town)
                return fusillade
            else:
                return None
        except Exception as e:
            print(f"Error_FusilladesDAO.findById() ::: {e}")

    def findAll(self) -> 'list[Fusillade]':
            try:
                query = '''SELECT * FROM Fusillades'''
                self.cursor.execute(query)
                res = self.cursor.fetchall()

                townDao = TownsDAO()
                fusillades = []
                
                if len(res)>0:

                    for r in res:
                        town = townDao.findById(r[6])

                        fusillade = Fusillade()
                        fusillade.setID(r[0])
                        fusillade.setStreetNumber(r[1])
                        fusillade.setStreetName(r[2])
                        fusillade.setAdditionalAddress(r[3])
                        fusillade.setDate(r[4])
                        fusillade.setDescription(r[5])
                        fusillade.setTown(town)
                        
                        fusillades.append(fusillade)

                    return fusillades

                else:

                    return []

            except Exception as e:
                print(f"Error_FusilladesDAO.findAll() ::: {e}")
    
    def insertOne(self, objIns: Fusillade) -> int:
        query = '''INSERT INTO Fusillades (street_number, street_name, additional_address, date, description, town_id) VALUES (%s, %s,%s,%s,%s,%s);'''
        values = (objIns.getStreetNumber(),objIns.getStreetName(), objIns.getAdditionalAddress(),objIns.getDate(),objIns.getDescription(),objIns.getTown().getID())
        error = "Erreur_FusilladesDAO.insertOne()"
        return super().operationTable(query, values,error)
        
    def update(self, id , objUpdated : Fusillade)->int:
        query = '''UPDATE Fusillades SET street_number = %s,street_name = %s, additional_address = %s,date = %s, description = %s,town_id = %s WHERE id = %s;'''
        values =  (objUpdated.getStreetNumber(),objUpdated.getStreetName(), objUpdated.getAdditionalAddress(),objUpdated.getDate(),objUpdated.getDescription(),objUpdated.getTown().getID(),id)
        error = "Erreur_FusilladesDAO.update()"
        return super().operationTable(query, values,error)

        
    def delete(self,id)->int:
        query = '''DELETE FROM Fusillades WHERE id = %s;'''
        values =  (id,)
        error = "Erreur_FusilladesDAO.delete()"
        return super().operationTable(query, values,error)
    