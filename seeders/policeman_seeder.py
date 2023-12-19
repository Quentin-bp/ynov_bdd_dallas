from seeders.Seeder import Seeder

class PolicemanSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO policemen (person_id, serial_numbers) VALUES 
        (4, '777LUCKYPLC');"""
