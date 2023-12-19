from seeders.Seeder import Seeder

class PersonSeeder(Seeder):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        INSERT INTO persons (last_name, first_name, genre, street_number, street_name, additional_address, town_id, nationality_id) VALUES 
        ('Perrier', 'Hugo', 0, '1 bis', 'Rue de la Paix', 'Bat. 7', 2, 1),
        ('Leclerc', 'Vanessa', 0, '7', 'Bd. de la Guerre', 'Etg. 10', 2, 1),
        ('Smith', 'William', 0, '465', 'Main Street', '', 1, 2),
        ('Phillix', 'Zack', 0, '789', 'Pine Lane', '', 1, 2),
        ('Jackson', 'Agata', 0, '101', 'Maple Joe Court', 'Flat 8888', 1, 2);"""

