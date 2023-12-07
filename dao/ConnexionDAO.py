import psycopg2  

class ConnexionBD:

    def __init__(self):
        self.cnx = None
        self.params = None

    def getConnexion(self):
        try:
            print("- class connexionBD() is running ... \n\n")
            print("- config/Config.yml is loading ...")

            # get file and data
            with open("/home/keke/DataspellProjects/lvmh_sephora/config/Config.yaml", "r") as fic:
                donnees = yaml.safe_load(fic)
            config = donnees["postgreSQLAccess"]
            db = config["database_name"]
            host = config["host"]
            port = config["port"]
            usr = config["user"]["usr1"]
            pwd = config["pwd"]["pwd1"]

            self.cnx = psycopg2.connect(dbname=db,
                                  host=host,
                                  port=port,
                                  user=usr,
                                  password=pwd
                                  )
            return self.cnx
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
        return self.cnx


