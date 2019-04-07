
class ElectronicDevice(object):
    def __init__(self,price):
        self.price = price

eD = ElectronicDevice(100)

class TV(ElectronicDevice):
    def __init__(self,price,resolution):
        ElectronicDevice.__init__(self,price)
        self.resolution = resolution

class Computer(ElectronicDevice):
    def __init__(self,price,numCPU):
        ElectronicDevice.__init__(self,price)
        self.numCPU = numCPU

class Laptop(Computer):
    def __init__(self,price,numCPU,batteryLife):
        Computer.__init__(self,price,numCPU)
        self.batteryLife = batteryLife

class Desktop(Computer):
    def __init__(self,price,numCPU,tower):
        Computer.__init__(self,price,numCPU)
        self.tower = tower
