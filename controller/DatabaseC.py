from migrations.Migrations import Migrations
from seeders.Seeders import Seeders
from roles.Roles import Roles
class DatabaseController:

    @staticmethod
    def createDatabase():
        migrations = Migrations()
        migrations.runAllMigrations()
        return "Executed"
    
    @staticmethod
    def insertData():
        seeders = Seeders()
        seeders.runAllSeeders()
        return "Executed"
    
    @staticmethod
    def createRoles() :
        roles = Roles()
        roles.createAllRoles()
        return "Executed"