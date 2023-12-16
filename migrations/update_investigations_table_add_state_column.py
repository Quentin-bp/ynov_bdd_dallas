
from migrations.Migration import Migration

class UpdateInvestigationsTableStateColumn(Migration):
      def __init__(self,connexion):
        super().__init__(connexion)
        self.query = """
        DO $$ BEGIN
          IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'status') THEN
            CREATE TYPE status AS ENUM ('classified', 'ongoing', 'without_follow-up');
            ALTER TABLE Investigations ADD COLUMN status status DEFAULT 'ongoing';
          END IF;
        END $$;"""