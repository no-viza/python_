#Classes (2)

class Vehicle: 
    __speed = 0

    def __init__(self, speed = 0): 
         self.__speed = speed

car1 = Vehicle(8)
#print(car1.__speed)

#Data Hiding
#add "__" to hide/protect the variable
#to access it
print(car1._Vehicle__speed)
#The best way to access it is by using "Getters and Setters"
#A private member is only accessible by itself in terms of attributes 

        