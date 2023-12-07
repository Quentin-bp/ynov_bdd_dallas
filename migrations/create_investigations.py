
from migrations.Migration import Migration

class CreateInvestigationsTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Investigations (
        id SERIAL PRIMARY KEY,
        advancement VARCHAR(1000),
        fusillade_id BIGINT,
        FOREIGN KEY (fusillade_id) REFERENCES Fusillades(id),
        );"""