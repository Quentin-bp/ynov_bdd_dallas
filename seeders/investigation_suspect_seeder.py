    
from seeders.Seeder import Seeder

class InvestigationSuspectSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO investigation_suspects (investigation_id, suspect_id) VALUES 
        (1, 1),
        (1, 2),
        (1, 3);"""

