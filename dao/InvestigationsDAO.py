from dao.ModelDAO import ModelDAO
from model.InvestigationsM import Investigation, InvestigationModel
from dao.FusilladesDAO import FusilladesDAO

from dao.PersonsDAO import PersonsDAO

from dao.ConnexionDAO import ConnexionBD


class InvestigationsDAO(ModelDAO):
    def __init__(self):
        params = ConnexionBD().getConnexion()
        #params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    def findById(self, id: int) -> Investigation:
            try:
                query = '''SELECT * FROM Investigations WHERE id = %s;'''
                fusilladeDAO = FusilladesDAO()

                self.cursor.execute(query, (id,))
                res = self.cursor.fetchone()
                if res:
                    fusillade = fusilladeDAO.findById(res[4])
                    investigation = Investigation()
                    investigation.setID(res[0])
                    investigation.setFusillade(res[1])
                    investigation.setAdvancement(res[2])
                    investigation.setStatus(res[3])
                    return investigation
                else:
                    return None
            except Exception as e:
                print(f"Error_InvestigationsDAO.findById() ::: {e}")

    def findAll(self) -> list[Investigation]:
            try:
                query = '''SELECT * FROM Investigations'''
                fusilladeDAO = FusilladesDAO()
                self.cursor.execute(query)
                res = self.cursor.fetchall()

                investigations = []

                if len(res) > 0:

                    for r in res:
                        fusillade = fusilladeDAO.findById(r[4])
                        investigation = Investigation()
                        investigation.setID(r[0])
                        investigation.setFusillade(r[1])
                        investigation.setAdvancement(r[2])
                        investigation.setStatus(r[3])

                        investigations.append(investigation)

                    return investigations

                else:

                    return []

            except Exception as e:
                print(f"Error_InvestigationsDAO.findAll() ::: {e}")

    def insertOne(self, objIns: Investigation) -> int:

            try:
                query = '''INSERT INTO Investigations (fusillade_id, advancement, status) VALUES (%s, %s, %s);'''
                self.cursor.execute(query, (objIns.getFusillade(), objIns.getAdvancement(), objIns.getStatus()))
                self.cursor.connection.commit()
                return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
            except Exception as e:
                print(f"Erreur_InvestigationsDAO.insertOne() ::: {e}")
                self.cursor.connection.rollback()
                return 0

    def update(self, id, objUpdated: Investigation) -> int:
            try:
                query = '''UPDATE Investigations SET fusillade_id = %s, advancement = %s, status = %s WHERE id = %s;'''
                self.cursor.execute(query, (objUpdated.getFusillade(), objUpdated.getAdvancement(), objUpdated.getStatus(), id))
                self.cursor.connection.commit()
                return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
            except Exception as e:
                print(f"Erreur_InvestigationsDAO.update() ::: {e}")
                self.cursor.connection.rollback()
                return 0

    def delete(self, id) -> int:
            try:
                query = '''DELETE FROM Investigations WHERE id = %s;'''
                self.cursor.execute(query, (id,))
                self.cursor.connection.commit()
                return self.cursor.rowcount if self.cursor.rowcount != 0 else 0
            except Exception as e:
                print(f"Erreur_InvestigationsDAO.delete() ::: {e}")
                self.cursor.connection.rollback()
                return 0

    def getActorsByInvestigationId(self, ObjInvId: int) -> 'list[Investigation]':
        try:
            query = '''SELECT DISTINCT
                            Investigations.id as id_enquete, Investigations.advancement as status_enquete, Investigation.fusillade_id as id_fusillade,
                            Policeman.role AS policeman_role, Policeman.first_name as agent_first_name,Policeman.last_name AS agent_last_name,
                            Suspect.role AS suspect_role, Suspect.first_name as suspect_first_name, Suspect.last_name AS suspect_last_name  
                        FROM
                            Investigations
                            JOIN Fusillades ON Investigations.fusillade_id = Fusillades.id
                            JOIN Persons AS policeman_person ON Fusillades.town_id = Policeman_Person.town_id
                            JOIN Policeman ON Policeman_Person.id = Policeman.id
                            JOIN Persons AS Suspect_Person ON Fusillade.town_id = Suspect_Person.town_id
                            JOIN "Suspect" ON Suspect_Person.id = Suspect.id
                        WHERE
                        Investigations.id = %s;'''
            fusilladeDAO = FusilladesDAO()

            self.cursor.execute(query, (ObjInvId,))
            res = self.cursor.fetchall()

            investigations = []
            if len(res) > 0:
                for r in res:
                    fusillade = fusilladeDAO.findById(res[2])
                    investigation = Investigation()
                    investigation.setID(r[0])
                    investigation.setFusillade(fusillade)
                    investigation.setAdvancement(r[1])

                    investigations.append(investigation)
                return investigations
            else:
                return []
        except Exception as e:
            print(f"Error_InvestigationsDAO.linkActorsBy_investigationId():::{e}")
        finally:
            self.cursor.close()


    # def getActorsByStatus(self, advancement: str) -> list[dict]:
    #         try:
    #             query = '''
    #                 SELECT DISTINCT
    #                     Investigations.id as id_enquete, Investigations.advancement as status_enquete, Investigations.fusillade_id as id_fusillade,
    #                     Policeman.role AS policeman_role, Policeman.first_name as agent_first_name,Policeman.last_name AS agent_last_name,
    #                     Suspect.role AS suspect_role, Suspect.first_name as suspect_first_name, Suspect.last_name AS suspect_last_name
    #                 FROM
    #                     Investigations
    #                     JOIN Fusillades ON Investigations.fusillade_id = Fusillades.id
    #                     JOIN Persons AS Policeman_Person ON Fusillades.town_id = Policeman_Person.town_id
    #                     JOIN Policeman ON Policeman_Person.id = Policeman.id
    #                     JOIN Persons AS Suspect_Person ON Fusillades.town_id = Suspect_Person.town_id
    #                     JOIN Suspect ON Suspect_Person.id = Suspect.id
    #                 WHERE
    #                     Investigation.advancement = %s;
    #             '''
    #
    #             self.cursor.execute(query, (advancement,))
    #             result = self.cursor.fetchall()
    #
    #             actors_list = []
    #             for row in result:
    #                 actor_info = {
    #                     "id_investigation": row["id_investigation"],
    #                     "status_investigation": row["status_investigation"],
    #                     "id_fusillade": row["id_fusillade"],
    #                     "policeman_role": row["policeman_role"],
    #                     "agent_first_name": row["agent_first_name"],
    #                     "agent_last_name": row["agent_last_name"],
    #                     "suspect_role": row["suspect_role"],
    #                     "suspect_first_name": row["suspect_first_name"],
    #                     "suspect_last_name": row["suspect_last_name"],
    #                 }
    #                 actors_list.append(actor_info)
    #
    #             return actors_list
    #
    #         except Exception as e:
    #             print(f"Erreur_InvestigationsDAO.link_actors_by_advancement():::{e}")
    #
    #         finally:
    #             self.cursor.close()


    def findByNameAndRole(self, last_name:str, first_name:str, role:str)->list:
        
        table_name = role # au singulier (policeman or suspect or jury)

        try:
            if table_name.lower() == 'policeman': 
                query = f'''
                    WITH investigation_overview as (
                        SELECT DISTINCT i.id, f.description, i.status, 
                                ps.last_name as policeman_last_name, ps.first_name as policeman_first_name, 
                                ps2.last_name as suspect_last_name, ps2.first_name as suspect_first_name, 
                                ps3.last_name as jury_last_name, ps3.first_name as jury_first_name
                        FROM Investigations i
                        INNER JOIN Investigation_Policemen ip ON i.id = ip.investigation_id
                        INNER JOIN Policemen p ON ip.policeman_id = p.id
                        INNER JOIN Persons ps ON p.person_id = ps.id
                        INNER JOIN Investigation_Suspects isus ON i.id = isus.investigation_id
                        INNER JOIN Suspects s ON isus.suspect_id = s.id
                        INNER JOIN Persons ps2 ON s.person_id = ps2.id
                        INNER JOIN Investigation_Juries ij ON i.id = ij.investigation_id
                        INNER JOIN Juries j ON ij.jury_id = j.id
                        INNER JOIN Persons ps3 ON j.person_id = ps3.id
                        INNER JOIN fusillades f ON i.fusillade_id = f.id)
                    SELECT * FROM investigation_overview
                    WHERE policeman_last_name LIKE %s AND policeman_first_name LIKE %s;'''

                values = (last_name, first_name,)
                self.cursor.execute(query, values)
                result = self.cursor.fetchall()

                investigation_overviews = []
                for row in result:
                    print(row)
                    investigation = {
                        'investigation_id': row[0],
                        'investigation_description': row[1],
                        'investigation_status': row[2],
                        'policeman':{
                            'last_name': row[3],
                            'first_name': row[4]
                        },
                        'suspect':{
                            'last_name': row[5],
                            'first_name': row[6]
                        },
                        'jury':{
                            'last_name': row[7],
                            'first_name': row[8]
                        }
                    }

                    investigation_overviews.append(investigation)
                
                return investigation_overviews

            elif table_name.lower() == 'suspect':
                query = f'''
                    WITH investigation_overview as (
                        SELECT DISTINCT i.id, f.description, i.status, 
                                ps.last_name as policeman_last_name, ps.first_name as policeman_first_name, 
                                ps2.last_name as suspect_last_name, ps2.first_name as suspect_first_name, 
                                ps3.last_name as jury_last_name, ps3.first_name as jury_first_name
                        FROM Investigations i
                        INNER JOIN Investigation_Policemen ip ON i.id = ip.investigation_id
                        INNER JOIN Policemen p ON ip.policeman_id = p.id
                        INNER JOIN Persons ps ON p.person_id = ps.id
                        INNER JOIN Investigation_Suspects isus ON i.id = isus.investigation_id
                        INNER JOIN Suspects s ON isus.suspect_id = s.id
                        INNER JOIN Persons ps2 ON s.person_id = ps2.id
                        INNER JOIN Investigation_Juries ij ON i.id = ij.investigation_id
                        INNER JOIN Juries j ON ij.jury_id = j.id
                        INNER JOIN Persons ps3 ON j.person_id = ps3.id
                        INNER JOIN fusillades f ON i.fusillade_id = f.id)
                    SELECT * FROM investigation_overview
                    WHERE suspect_last_name LIKE %s AND suspect_first_name LIKE %s;'''

                values = (last_name, first_name,)
                self.cursor.execute(query, values)
                result = self.cursor.fetchall()

                investigation_overviews = []
                for row in result:
                    investigation = {
                        'investigation_id': row[0],
                        'investigation_description': row[1],
                        'investigation_status': row[2],
                        'policeman':{
                            'last_name': row[3],
                            'first_name': row[4]
                        },
                        'suspect':{
                            'last_name': row[5],
                            'first_name': row[6]
                        },
                        'jury':{
                            'last_name': row[7],
                            'first_name': row[8]
                        }
                    }

                    investigation_overviews.append(investigation)
                
                return investigation_overviews

            elif table_name.lower() == 'jury': 
                query = f'''
                    WITH investigation_overview as (
                        SELECT DISTINCT i.id, f.description, i.status, 
                                ps.last_name as policeman_last_name, ps.first_name as policeman_first_name, 
                                ps2.last_name as suspect_last_name, ps2.first_name as suspect_first_name, 
                                ps3.last_name as jury_last_name, ps3.first_name as jury_first_name
                        FROM Investigations i
                        INNER JOIN Investigation_Policemen ip ON i.id = ip.investigation_id
                        INNER JOIN Policemen p ON ip.policeman_id = p.id
                        INNER JOIN Persons ps ON p.person_id = ps.id
                        INNER JOIN Investigation_Suspects isus ON i.id = isus.investigation_id
                        INNER JOIN Suspects s ON isus.suspect_id = s.id
                        INNER JOIN Persons ps2 ON s.person_id = ps2.id
                        INNER JOIN Investigation_Juries ij ON i.id = ij.investigation_id
                        INNER JOIN Juries j ON ij.jury_id = j.id
                        INNER JOIN Persons ps3 ON j.person_id = ps3.id
                        INNER JOIN fusillades f ON i.fusillade_id = f.id)
                    SELECT * FROM investigation_overview
                    WHERE jury_last_name LIKE %s AND jury_first_name LIKE %s;'''

                values = (last_name, first_name,)
                self.cursor.execute(query, values)
                result = self.cursor.fetchall()

                investigation_overviews = []
                for row in result:
                    investigation = {
                        'investigation_id': row[0],
                        'investigation_description': row[1],
                        'investigation_status': row[2],
                        'policeman':{
                            'last_name': row[3],
                            'first_name': row[4]
                        },
                        'suspect':{
                            'last_name': row[5],
                            'first_name': row[6]
                        },
                        'jury':{
                            'last_name': row[7],
                            'first_name': row[8]
                        }
                    }

                    investigation_overviews.append(investigation)
                
                return investigation_overviews
            else:
                return ['Role does not exist in database']
        except Exception as e:
            #raise e
            print(f'Erreur_investigationsDAO.findByNameAndRole() ::: {e}')

    


