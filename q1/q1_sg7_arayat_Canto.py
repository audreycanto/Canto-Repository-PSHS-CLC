"""
Canto, Louise Audreana B. (#20)
9-Arayat
09/16/2026
"""

class Glassware:
    def __init__(self, kindofglassware):
        self.kindofglassware = kindofglassware
        
class Beaker(Glassware):
    def __init__(self, kindofglassware):
        super().__init__(kindofglassware)
       

class Tray(Glassware):
    def __init__(self):
        self.beakers = []
        for i in range (5):
            self.beakers.append(Beaker("beaker"))

my_tray = Tray()

print(f"You have {len(my_tray.beakers)} beakers.")

