import random


class Ore():
    name: str
    priority: int
    dificulty: int

    def __init__(self, name):
        self.name = name
        self.priority = self.get_priority()
        self.dificulty = self.get_dificulty()

    def get_priority(self):
        table = {
            'cobre':1,
            'ferro':2,
            'ouro':3,
            'redstone':4,
            'diamante':5
        }
        priority = table.get(self.name, 0)
        return priority

    def get_dificulty(self):
        dificulty = random.choice([1,2,3,4,5]) * self.priority
        return dificulty