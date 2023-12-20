
from roles.Role import Role

class CreateCommissionerRole(Role):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE ROLE commissioner;"""