
from roles.Role import Role

class CreateInvestigatorRole(Role):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE ROLE investigator;"""