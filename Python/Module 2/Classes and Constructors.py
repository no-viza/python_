#Example of a class

#a Class allows us to group code

class Vehicle: #(object)
    #Attribute(below)
    speed = 1
    distance = 0
#contructor
    #def __new__(cls):
    #    return object.__new__(cls)

#the "self" keyword automatically passes in the Instance of a class in python

#the init(initializatio) method is better as it has access to all the attributes and methods of the created class
#the init is an example of a method overload
    def __init__(self, speed = 0): 
         self.speed = speed
        
    #Method(below)
    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount 
    def IncreaseDistance(self, increaseDis):
        self.distance += increaseDis 

    def __add__(Self, otherVehicle):
        return Vehicle(Self.speed + otherVehicle.speed)

    def __del__(self):
        print("deleted")  

class Car(Vehicle):
    weight = 1000

    def IncreaseWeight(self, weight):
        self.weight += weight 
    #overridng methods (below)
    def IncreaseSpeed(self, increaseAmount):
        self.speed *= increaseAmount 


#Creating Instance Objects

car = Vehicle()
truck = Vehicle(16)
bus = Vehicle()
train = Vehicle()
ECar = Car(5)

print(ECar.weight)
ECar.IncreaseWeight(200)
print(ECar.weight)
ECar.IncreaseSpeed(5)
print(ECar.speed)

print("-----------")

#Accessing Attributes

print("speed for car: %i" % car.speed)
car.IncreaseSpeed(25)
print("speed for car: %i" % car.speed)

print("speed for truck: %i" %  truck.speed)
truck.IncreaseSpeed(15)
print("speed for truck: %i" %  truck.speed)

print("-----------")

bike = car + truck 
print(bike.speed)
#the bike is the object created by the addition of 2 other oebjects 

#Constructors and "Init" method

#Constructors are methods that are called when class is first created

#Destroying objects
#del = delete
#del truck
#destructors are called at the end of a class

#Class Inheritance 

#Overloading Methods
#it is to change the default functionality of a method

#overriding methods
#it means to override an existing method
#the child class inherit the functionality of its parent class but can be modified (override)

#Overloading Operators 
#operators: "+", "=" etc.

