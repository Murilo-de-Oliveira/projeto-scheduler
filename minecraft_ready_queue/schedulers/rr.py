import time
from app.ores import Ore

class SchedulerRoundRobin:
    def __init__(self, ores):
        self.fila = ores
        self.quantum = 2  # Tempo de CPU alocado para cada minério

    def processar(self):
        index = 0
        total_tempo = -2
        while any(ore.dificulty > 0 for ore in self.fila):
            ore = self.fila[index]
            print(f"Processando {ore.name} por {min(self.quantum, ore.dificulty):.2f} segundos")

            total_tempo += 2
            # Simula o processamento pelo tempo do quantum ou o tempo restante
            tempo_processamento = min(self.quantum, ore.dificulty)
            time.sleep(tempo_processamento)
            ore.dificulty -= tempo_processamento

            # Move para o próximo minério
            index = (index + 1) % len(self.fila)

        print("Todos os minérios foram processados.")
        return total_tempo/len(self.fila)