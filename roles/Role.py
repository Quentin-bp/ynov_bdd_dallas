

class Role :
    def __init__(self,connexion):
        self.query = ""
        self.conn = connexion

    def execute(self):
        conn = self.conn.getConnexion()
        cursor = conn.cursor()
        cursor.execute(self.query)
        cursor.close()
        conn.commit()
        conn.close()