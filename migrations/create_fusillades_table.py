
from migrations.Migration import Migration

class CreateFusilladesTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Fusillades (
        id SERIAL PRIMARY KEY,
        town_id BIGINT,
        address VARCHAR(255),
        date DATE,
        description VARCHAR(1000),
        FOREIGN KEY (town_id) REFERENCES Towns(id) ON UPDATE CASCADE ON DELETE CASCADE,
        );"""