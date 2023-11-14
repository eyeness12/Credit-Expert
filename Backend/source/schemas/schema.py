from pydantic import BaseModel

class Info(BaseModel):
    TC: str
    age: int
    SN: float
    TM: float
    PrêtD:float
    ResteAVivre :float
    PF:str

class EInfo(BaseModel):
    EBE: float
    ET: float
    CP: float
    TA: float
    RD: float
    FF: float
    CA: float
    FP: float
    VA: float

class PredictionOutput(BaseModel):
    response:str
    




