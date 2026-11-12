from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class TempSensor(Sensor):
    def get_data(self):
        return "24°C"
    def __str__(self):
        return "24°C"
    
tempSensor = TempSensor()
print(tempSensor)
