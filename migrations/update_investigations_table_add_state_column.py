
from migrations.Migration import Migration

class UpdateInvestigationsTableStateColumn(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        CREATE TYPE status AS ENUM ('classified','ongoing', 'follow-up');
        ALTER TABLE Investigations ADD status status DEFAULT 'ongoing';"""