from pydantic import BaseModel
from typing import List

class MinerioData(BaseModel):
    minerios: List[str]
    quantidades: List[int]

class ResultadoProcessamento(BaseModel):
    algoritmo: str
    tempo_medio_espera: float
    tempo_total: float
    minerios_processados: List[str]
