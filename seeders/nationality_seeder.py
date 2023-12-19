from seeders.Seeder import Seeder

class NationalitySeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO nationalities (name) VALUES 
        ('Français'), 
        ('Américain');"""