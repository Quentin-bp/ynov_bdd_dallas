from seeders.Seeder import Seeder

class FusilladeSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO fusillades (street_number, street_name, additional_address, date, description, town_id) VALUES 
         ('482', 'Oak Avenue', '', '2007-02-21', 'It started in the morning at 09:17 near the traffic jam and ended near 09:45. Two people were injuried. No deaths.', 1);"""

