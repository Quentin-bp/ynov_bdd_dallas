
from migrations.Migration import Migration

class CreateTownsTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Towns (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        address_code VARCHAR(255),
        town_id BIGINT,
        FOREIGN KEY (town_id) REFERENCES Towns(id) ON UPDATE CASCADE ON DELETE CASCADE,
        nationality_id BIGINT ,
        FOREIGN KEY (nationality_id) REFERENCES Nationalities(id) ON UPDATE CASCADE ON DELETE CASCADE,
        );"""