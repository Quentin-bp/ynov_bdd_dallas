from migrations.Migrations import Migrations

class DatabaseController:

    @staticmethod
    def createDatabase():
        migrations = Migrations()
        migrations.runAllMigrations()
        return "Executed"