import psycopg2  # pip install psycopg2-binary
from decouple import Config, RepositoryEnv

DOTENV_FILE = './config/.env'

class ConnexionBD:

    def __init__(self):
        self.cnx = None
        self.params = None

    def getConnexion(self):
        try:
            print("- class connexionBD() is running ... \n\n")
            # get file and data
            env_config = Config(RepositoryEnv(DOTENV_FILE))
            db = env_config.get("DATABASE_NAME")
            host = env_config.get("HOST")
            port = env_config.get("PORT")
            username = env_config.get("LOGIN_DATABASE")
            password = env_config.get("PASSWORD_DATABASE")

            self.cnx = psycopg2.connect(dbname=db,
                                  host=host,
                                  port=port,
                                  user=username,
                                  password=password
                                  )
            return self.cnx
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
            raise e
        #return self.cnx

