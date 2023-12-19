from .town_seeder import TownSeeder
from .nationality_seeder import NationalitySeeder

from .person_seeder import PersonSeeder
from .jury_seeder import JurySeeder
from .policeman_seeder import PolicemanSeeder
from .suspect_seeder import SuspectSeeder

from .investigation_seeder import InvestigationSeeder

from .investigation_policeman_seeder import InvestigationPolicemanSeeder
from .investigation_jury_seeder import InvestigationJurySeeder
from .investigation_suspect_seeder import InvestigationSuspectSeeder

from .fusillade_seeder import FusilladeSeeder
from dao import ConnexionDAO


class Seeders :
    def __init__(self):
        self.conn = ConnexionDAO.ConnexionBD()

    def getAllSeeders(self):
        towns = TownSeeder(self.conn)
        nationalities = NationalitySeeder(self.conn)
        persons = PersonSeeder(self.conn)
        
        policemen = PolicemanSeeder(self.conn)
        suspects = SuspectSeeder(self.conn)
        juries = JurySeeder(self.conn)
        
        fusillades = FusilladeSeeder(self.conn)
        investigations = InvestigationSeeder(self.conn)

        investigations_suspects = InvestigationSuspectSeeder(self.conn)
        investigations_policemen = InvestigationPolicemanSeeder(self.conn)
        investigations_juries = InvestigationJurySeeder(self.conn)
 
        return [
            towns,
            nationalities,
            persons,

            policemen,
            suspects,
            juries,

            fusillades,
            investigations,

            investigations_suspects,
            investigations_policemen,
            investigations_juries
        ]
    
    def runAllSeeders(self):
        seeders = self.getAllSeeders()
        
        ##########################
        print("Load seeders")
        ##########################
        for seeder in seeders:
            seeder.execute()
        ##########################
        print("Seeders loaded")
        ##########################
