from seeders.Seeder import Seeder

class InvestigationSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO investigations (advancement, fusillade_id) VALUES 
        ('Enquête ouverte à ce jour.', 1);"""