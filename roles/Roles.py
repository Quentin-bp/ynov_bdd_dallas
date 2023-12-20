from .create_role_commissioner import CreateCommissionerRole
from .create_role_investigator import CreateInvestigatorRole
from dao import ConnexionDAO


class Roles :
    def __init__(self):
        self.conn = ConnexionDAO.ConnexionBD()

    def getAllRoles(self):
        create_commissioner = CreateInvestigatorRole(self.conn)
        create_investigator = CreateCommissionerRole(self.conn)
        return [
            create_commissioner,
            create_investigator, 
        ]
    
    def createAllRoles(self):
        roles = self.getAllRoles()
        
        ##########################
        print("Load roles")
        ##########################
        for role in roles:
            role.execute()
        ##########################
        print("Roles loaded")
        ##########################
