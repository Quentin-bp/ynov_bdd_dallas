from dao.ModelDAO import ModelDAO
from model.UsersM import UserModel

class UsersDAO(ModelDAO):
    def __init__(self):
        
        params = ModelDAO.connect_objet
        self.cursor = params.cursor()

    def createUserCommissioner(self, user: UserModel) -> int:
            try:
                query = f'''create user {user.name} with password '{user.pwd}';'''
                self.cursor.execute(query)
                self.cursor.connection.commit()

                query_role = f'''grant commissioner to {user.name};'''
                self.cursor.execute(query_role)
                self.cursor.connection.commit()
                
                return self.cursor.rowcount if self.cursor.rowcount !=0 else 0
            except Exception as e:
                print(f"Error_UsersDAO.createUserCommissioner) ::: {e}")
                self.cursor.connection.rollback()
            finally:
                self.cursor.close()

    def checkUserCommissioner(self, user_name):
        try:
            query = """ SELECT r.rolname
                        FROM pg_user u
                        JOIN pg_auth_members m ON u.usesysid = m.member
                        JOIN pg_roles r ON m.roleid = r.oid
                        WHERE u.usename = %s;"""
            
            self.cursor.execute(query,(user_name,))
            self.cursor.connection.commit()
            
            res = self.cursor.fetchone()
            print(res)
            if res :
                if 'commissioner' in res:
                    return True
            return False
        
        except Exception as e:
            print(f"Error_UsersDAO.checkUserCommissioner) ::: {e}")
            self.cursor.connection.rollback()
            
    def insertOne(self, objIns: list[int])->int:
        pass

    def findAll(self)->list:
        pass

    def update(self,id,objUpdated)->int:
        pass

    def delete(self,id)->int:
        pass        