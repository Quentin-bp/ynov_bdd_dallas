
from migrations.Migration import Migration

class CreateJuriesTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Juries (
        id SERIAL PRIMARY KEY,
        person_id BIGINT,
        FOREIGN KEY (person_id) REFERENCES Persons(id) ON UPDATE CASCADE ON DELETE CASCADE
        );"""