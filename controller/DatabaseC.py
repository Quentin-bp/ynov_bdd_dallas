from migrations.Migrations import Migrations
from seeders.Seeders import Seeders
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