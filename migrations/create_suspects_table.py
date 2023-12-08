from migrations.Migration import Migration

class CreateSuspectsTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Suspects (
        id SERIAL PRIMARY KEY,
        person_id BIGINT,
        verdict VARCHAR(1000),
        FOREIGN KEY (person_id) REFERENCES Persons(id) ON UPDATE CASCADE ON DELETE CASCADE
        );"""