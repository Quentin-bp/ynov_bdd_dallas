
from migrations.Migration import Migration

class CreatePersonsTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Persons (
        id SERIAL PRIMARY KEY,
        last_name VARCHAR(255),
        first_name VARCHAR(255),
        genre INTEGER,
        street_number VARCHAR(255),
        street_name VARCHAR(255),
        additional_address VARCHAR(255),
        nationality_id BIGINT,
        FOREIGN KEY (nationality_id) REFERENCES Nationalities(id) ON UPDATE CASCADE ON DELETE CASCADE

        );"""