from .create_towns_table import CreateTownsTable
from .create_nationalities_table import CreateNationalitiesTable
from .create_persons_table import CreatePersonsTable

from .create_policemen_table import CreatePolicemenTable
from .create_suspects_table import CreateSuspectsTable
from .create_juries_table import CreateJuriesTable

from .create_fusillades_table import CreateFusilladesTable
from .create_investigations_table import CreateInvestigationsTable


from dao import ConnexionDAO


class Migrations :
    def __init__(self):
        self.conn = ConnexionDAO.ConnexionBD()

    def getAllMigrations(self):
        create_towns = CreateTownsTable(self.conn)
        create_nationalities = CreateNationalitiesTable(self.conn)
        create_persons = CreatePersonsTable(self.conn)
        
        create_policemen = CreatePolicemenTable(self.conn)
        create_suspects = CreateSuspectsTable(self.conn)
        create_juries = CreateJuriesTable(self.conn)
        
        create_fusillades = CreateFusilladesTable(self.conn)
        create_investigations = CreateInvestigationsTable(self.conn)

        return [
            create_towns,
            create_nationalities,
            create_persons,

            create_policemen,
            create_suspects,
            create_juries,

            create_fusillades,
            create_investigations
        ]
    
    def runAllMigrations(self):
        migrations = self.getAllMigrations()
        
        ##########################
        print("Load migrations")
        ##########################
        for migration in migrations:
            migration.execute()
        ##########################
        print("Migrations loaded")
        ##########################
