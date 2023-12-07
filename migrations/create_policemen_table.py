from migrations.Migration import Migration

class CreatePolicemenTable(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """CREATE TABLE IF NOT EXISTS Policemen (
        id SERIAL PRIMARY KEY,
        person_id BIGINT,
        serial_numbers VARCHAR(255),
        FOREIGN KEY (person_id) REFERENCES Persons(id) ON UPDATE CASCADE ON DELETE CASCADE,
        );"""