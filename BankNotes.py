

from pydantic import BaseModel

class BankNote(BaseModel):
    variance : float
    skeness : float
    curtosis : float
    entropy : float
