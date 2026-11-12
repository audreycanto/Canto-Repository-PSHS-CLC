"""
Canto, Louise Audreana B.
9-Arayat
"""

from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"
    def __str__(self):
        return "7.2 pH"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"
    def __str__(self):
        return "24.5°C"
    
tempSensor = TempSensor()
pHsensor = PHSensor()

print("--- Lab Inventory System ---")
print(f"[pH Sensor] Reading: {pHsensor} (Neutral)")
print(f"[Temperature Sensor] Reading: {tempSensor}")
print("\n----------------------------")
