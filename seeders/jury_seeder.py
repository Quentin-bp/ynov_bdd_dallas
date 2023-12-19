from seeders.Seeder import Seeder

class JurySeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO juries (person_id) VALUES 
        (5);"""