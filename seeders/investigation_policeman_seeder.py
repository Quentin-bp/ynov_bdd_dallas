from seeders.Seeder import Seeder

class InvestigationPolicemanSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO investigation_policemen (investigation_id, policeman_id) VALUES 
        (1, 1);"""