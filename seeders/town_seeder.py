from seeders.Seeder import Seeder

class TownSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO towns (name, postal_code) VALUES 
        ('Dallas', '752000'), 
        ('Nanterre', '92001');"""