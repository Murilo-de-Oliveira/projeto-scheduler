# app/main.py
from fastapi import FastAPI
from .models import MinerioData
#from .schedulers import processar_round_robin, processar_fsfc

app = FastAPI()

@app.post("/process-minerios")
async def process_minerios(data: MinerioData):
    # Chama as funções de processamento
    #resultados_rr = processar_round_robin(data.minerios, data.quantidades)
    #resultados_fsfc = processar_fsfc(data.minerios, data.quantidades)
    """
    return {
        "round_robin": resultados_rr,
        "fsfc": resultados_fsfc
    }
    """

# Para rodar o servidor: uvicorn app.main:app --reload
