from datetime import date
today = date.today()
from dateutil.relativedelta import *
import numpy as np




class Person(object):
    def __init__(self, name, birthdate):
        self.birthdate = birthdate
        self.name = name
    def __str__(self):
        return """ My name is {name}
and I am {age} old""".format(name=self.name,age=self.calcAge().years)
    def calcAge(self):
        age = relativedelta(date.today(), self.birthdate)
        return age
        



# class Policyholder(Person):
#     def __init__(self, name, birthdate):
#         Person.__init__(self,name,birthdate)




# class CarOwner(Person):
#     def __init__(self, name, birthdate):
#         Person.__init__(self,name, birthdate)


class Vehicle(object):
    def __init__(self,firstRegistration,power,carOwner,make,model):
        self.firstRegistration = firstRegistration
        self.power = power
        self.carOwner = carOwner
        self.make = make
        self.model = model
    def __str__(self):
        rstr = """Make : {make} 
        Model : {model}
        Horse Power : {power}
        Age : {age} years old
        """.format(age=self.calcAge().years,make=self.make,model=self.model,power=self.power)
        return rstr
    def calcAge(self):
        age = relativedelta(date.today(), self.firstRegistration)
        return age
        



class Car(Vehicle):
    numWheels = 4
    def __init__(self,firstRegistration,power,carOwner,make,model):
        Vehicle.__init__(self,firstRegistration,power,carOwner,make,model)





class Motorbike(Vehicle):
    numWheels = 4
    def __init__(self,firstRegistration,power,carOwner,make,model):
        Vehicle.__init__(self,firstRegistration,power,carOwner,make,model)


class Tariff(object):
    def __init__(self,fixedCosts,riskPremium):
        self.fixedCosts = fixedCosts
        self.riskPremium = riskPremium
    def getScores(self,contract):
        
        scoresum = 0
        d_score = ""
        d_ph = {"age" : contract.policyholder.calcAge().years}
        if d_ph["age"] > 25:
            age_score = 1.00
        else:
            age_score = 1.25
        d_veh = {'age': contract.vehicle.calcAge().years}

        if d_veh['age'] == 0:
            veh_age_score = 0.8
        else:
            veh_age_score = 1.00
        d_score = {"age":age_score,
        "veh_age":veh_age_score
         } 

        scoresum = np.product(list(d_score.values()))

        return d_score, scoresum





class Contract(object):
    def __init__(self,inception,policyholder,vehicle,tariff):
        self.inception = inception
        self.policyholder = policyholder
        self.vehicle = vehicle
        self.tariff = tariff
    def getPrice(self):
        d_score,scoresum = self.tariff.getScores(self)
        price = self.tariff.fixedCosts + self.tariff.riskPremium*scoresum
        return price
        # print(scoresum)"""

    def __str__(self):
        print ('CONTRACT DETAILS')
        print('VEHICLE DETAILS')
        print(self.vehicle)
        print('Policyholder DETAILS')
        print(self.policyholder)
        print("PREMIUM")
        print(self.getPrice())
        return ""


# Init persons


john = Person('John',date(2000, 10, 5))
print(john)
mary = Person('Mary',date(1980, 12, 1))
print(mary)

# Init Vehicles


toyota = Car(
    firstRegistration = date(2005,1,1),
    power=100,
    carOwner = john,
    make = "Toyota",
    model = "Prius"

    )
print(toyota)
bmw = Motorbike(
    firstRegistration = date.today(),
    power=250,
    carOwner = mary,
    make = "BMW",
    model = "HP4"

    )
print(bmw)

# Init Tariffs

tariff_motobike = Tariff(fixedCosts=100,riskPremium=125)
tariff_car = Tariff(fixedCosts=100,riskPremium=250)

# Init Contracts

contract1 = Contract(date(2019,1,1),john,toyota,tariff_car)
contract2 = Contract(date(2019,1,1),mary,bmw,tariff_motobike)


# Print Results
print(contract1)

print(contract2)