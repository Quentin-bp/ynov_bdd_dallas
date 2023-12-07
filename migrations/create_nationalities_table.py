
from migrations.Migration import Migration

class CreateNationalitiesTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Nationalities (
        id SERIAL PRIMARY KEY,
        name VARCHAR(1000),
        );"""