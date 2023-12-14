
from migrations.Migration import Migration

class CreateInvestigationsJuriesTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Investigation_Juries (
        id SERIAL PRIMARY KEY,
        investigation_id BIGINT,
        FOREIGN KEY (investigation_id) REFERENCES Investigations(id) ON UPDATE CASCADE ON DELETE CASCADE,
        jury_id BIGINT,
        FOREIGN KEY (jury_id) REFERENCES Juries(id) ON UPDATE CASCADE ON DELETE CASCADE
        );"""