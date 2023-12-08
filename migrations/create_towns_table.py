
from migrations.Migration import Migration

class CreateTownsTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Towns (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        postal_code VARCHAR(255)
        );"""