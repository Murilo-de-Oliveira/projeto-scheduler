import time
from app.ores import Ore

class ProcessadorFCFS:
    def __init__(self, ores):
        self.queue = ores

    def processar(self):
        tempo_espera = 0
        for i, ore in enumerate(self.queue):
            # Simula o tempo de processamento com base na dificuldade
            tempo_processamento = ore.dificulty/10  # Ajuste o divisor conforme necessário
            print(f"Iniciando processamento de {ore.name}...")
            time.sleep(tempo_processamento)  # Simula o tempo de processamento
            print(f"Processamento concluído para {ore.name} com prioridade {ore.priority} e dificuldade {ore.dificulty}")
            if i > 0:
                tempo_espera += tempo_processamento
        return tempo_espera/(len(self.queue)-1)