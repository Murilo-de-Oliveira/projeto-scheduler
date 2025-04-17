import random
from app.ores import Ore
from schedulers.fcfs import ProcessadorFCFS

list_ores = []
for i in range(1,10):
    name = random.choice(['cobre','ferro','ouro','redstone','diamante'])
    ore = Ore(name)
    list_ores.append(ore)

for ore in list_ores:
    print(ore.name, ore.priority, ore.dificulty)

print(f"Tempo de espera médio: {ProcessadorFCFS(list_ores).processar()} segundos")
