import pprint
import random
from app.ores import Ore
from schedulers.fcfs import SchedulerFCFS
from schedulers.ps import SchedulerPS
from schedulers.sjf import SchedulerSJF
from schedulers.rr import SchedulerRoundRobin


list_ores = []
for i in range(1,10):
    name = random.choice(['cobre','ferro','ouro','redstone','diamante'])
    ore = Ore(name)
    list_ores.append(ore)

for ore in list_ores:
    print(ore.name, ore.priority, ore.dificulty)

new_dict = {
    'First Come First Served': SchedulerFCFS(list_ores).processar(),
    'Priority Scheduling': SchedulerPS(list_ores).processar(),
    'Shortest Job First': SchedulerSJF(list_ores).processar(),
    'Round Robin': SchedulerRoundRobin(list_ores).processar()
    }

pprint.pprint(new_dict)