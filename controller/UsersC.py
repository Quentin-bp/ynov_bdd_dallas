from dao.UsersDAO import UsersDAO
from model.UsersM import UserModel

class UsersController:
    @staticmethod
    def createUserCommissioner(user: UserModel):
        try:
            dao=UsersDAO()
            res = dao.createUserCommissioner(user)

            if res == 0:
                return "ERROR"

            return "User Added"

        except Exception as e:
            print(f"Error_InvestigationsC.createUserCommissioner():::{e}")
            return None