from seeders.Seeder import Seeder

class InvestigationJurySeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO investigation_juries  (investigation_id, jury_id) VALUES 
         (1, 1);"""