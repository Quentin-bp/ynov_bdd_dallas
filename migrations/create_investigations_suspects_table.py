
from migrations.Migration import Migration

class CreateInvestigationsSuspectsTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Investigation_Suspects (
        id SERIAL PRIMARY KEY,
        investigation_id BIGINT,
        FOREIGN KEY (investigation_id) REFERENCES Investigations(id) ON UPDATE CASCADE ON DELETE CASCADE,
        suspect_id BIGINT,
        FOREIGN KEY (suspect_id) REFERENCES Suspects(id) ON UPDATE CASCADE ON DELETE CASCADE
        );"""