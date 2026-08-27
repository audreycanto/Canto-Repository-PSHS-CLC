"""
Canto, Louise Audreana B. (#20)
9-Arayat
08/27/2026
"""

class Hero:
     def __init__(self, name, hp=100):
         self.name = name
         self.hp = hp
     def take_damage(self, amount):
         self.hp = self.hp - amount
         print(f"{self.name} took {amount} damage!")
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)
print(arthur.name,"'s HP:",arthur.hp)
print(morgana.name,"'s HP:", morgana.hp)
