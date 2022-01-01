def x(hp):
    if hp <= 0:
        print('player lost')
    else:
        return hp


class Character:
    def __init__(self, name):
        self.name = name
        self.hp_max = 100
        self.hp_current = x(self.hp_max)
        self.damage = 10

    def attack(self, target):
        target.hp_current = target.hp_current - self.damage

