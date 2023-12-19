from seeders.Seeder import Seeder

class SuspectSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO suspects (person_id, verdict) VALUES 
        (1, ''), 
        (2, ''),
        (3, '');"""