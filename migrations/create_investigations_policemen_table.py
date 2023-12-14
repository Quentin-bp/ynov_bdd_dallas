
from migrations.Migration import Migration

class CreateInvestigationsPolicemenTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Investigation_Policemen (
        id SERIAL PRIMARY KEY,
        investigation_id BIGINT,
        FOREIGN KEY (investigation_id) REFERENCES Investigations(id) ON UPDATE CASCADE ON DELETE CASCADE,
        policeman_id BIGINT,
        FOREIGN KEY (policeman_id) REFERENCES Policemen(id) ON UPDATE CASCADE ON DELETE CASCADE
        );"""