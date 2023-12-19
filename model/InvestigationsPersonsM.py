from pydantic import BaseModel

class InvestigationSuspect(BaseModel):
    investigation_id : int
    suspect_id : int

class InvestigationPoliceman(BaseModel):
    investigation_id : int
    policeman_id : int


class InvestigationJury(BaseModel):
    investigation_id : int
    jury_id : int

class InvestigationResearch(BaseModel):
    first_name: str
    last_name: str
    role: str