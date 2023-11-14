from fastapi import APIRouter
from source.schemas.schema import Info, EInfo
from configuration.injection import facts , PersonalInfo ,factsE, Ratios , LoanAcceptance
from source.services.personnel_service import LoanEvaluation 
from source.services.business_service import LoanEvaluationE
from source.schemas.schema import PredictionOutput

import sys
import io


credit_router=APIRouter()

@credit_router.post('/v1/personnel_credit',response_model=PredictionOutput)
async def evaluate_loan(info: Info):
    engine = LoanEvaluation()
    engine.reset()
    personal_info = PersonalInfo(
        TypeContrat=info.TC,
        age=info.age,
        SalaireNet=info.SN,
        TotalMensualités=info.TM,
        PrêtDemandé=info.PrêtD,
        ResteAVivre=info.ResteAVivre,
        PasDeFichageBanqueDeFrance=info.PF,
        )
    TauxEndettement = (info.TM* 100) / info.SN
    personal_info["TauxEndettement"] = TauxEndettement

    for fact in facts:
        engine.declare(fact)
    for key, value in personal_info.items():
        engine.declare(PersonalInfo(**{key: value}))
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    engine.run()
    sys.stdout = sys.__stdout__
    output_text = output_buffer.getvalue()
    output_buffer.close()
    paragraphs = output_text.split("\n")
    list=[]
    print(paragraphs)
    for word in paragraphs:
        if "loan" in word:
            return{"response":word}

@credit_router.post('/v1/business_credit',response_model=PredictionOutput)
async def evaluate_loan(info: EInfo):
    print(info)
    ratios_data = Ratios(R1=info.EBE/info.ET, R2=info.CP/info.TA, R3=info.RD/info.TA, R4=info.FF/info.CA, R5=info.FP/info.VA)
    
    engine = LoanEvaluationE()
    engine.reset()
    engine.declare(ratios_data)
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    engine.run()
    sys.stdout = sys.__stdout__
    output_text = output_buffer.getvalue()
    output_buffer.close()
    paragraphs = output_text.split("\n")
    return{ "response": paragraphs[0]}
    

   
    