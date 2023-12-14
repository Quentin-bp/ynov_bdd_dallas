from .create_towns_table import CreateTownsTable
from .create_nationalities_table import CreateNationalitiesTable
from .create_persons_table import CreatePersonsTable

from .create_policemen_table import CreatePolicemenTable
from .create_suspects_table import CreateSuspectsTable
from .create_juries_table import CreateJuriesTable

from .create_fusillades_table import CreateFusilladesTable
from .create_investigations_table import CreateInvestigationsTable

from .create_investigations_policemen_table import CreateInvestigationsPolicemenTable
from .create_investigations_juries_table import CreateInvestigationsJuriesTable
from .create_investigations_suspects_table import CreateInvestigationsSuspectsTable

from .update_investigations_table_add_state_column import UpdateInvestigationsTableStateColumn
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

        create_investigations_suspects = CreateInvestigationsSuspectsTable(self.conn)
        create_investigations_policemen = CreateInvestigationsPolicemenTable(self.conn)
        create_investigations_juries = CreateInvestigationsJuriesTable(self.conn)

        update_investigations_table_add_state_column = UpdateInvestigationsTableStateColumn(self.conn)
        return [
            create_towns,
            create_nationalities,
            create_persons,

            create_policemen,
            create_suspects,
            create_juries,

            create_fusillades,
            create_investigations,

            create_investigations_suspects,
            create_investigations_policemen,
            create_investigations_juries,

            update_investigations_table_add_state_column
            
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
