
class Hero:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp = self.hp - amount
Arthur = Hero(Arthur, 100)
Morgana = Hero(Morgana, 100)
Arthur.takedamage(10)
print("Arthur's hp", self.hp)
print("Morgana's hp", self.hp)
        
