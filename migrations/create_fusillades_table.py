
from migrations.Migration import Migration

class CreateFusilladesTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Fusillades (
        id SERIAL PRIMARY KEY,
        street_number VARCHAR(255),
        street_name VARCHAR(255),
        additional_address VARCHAR(255),
        date DATE,
        description VARCHAR(1000),
        town_id BIGINT,
        FOREIGN KEY (town_id) REFERENCES Towns(id) ON UPDATE CASCADE ON DELETE CASCADE
        );"""