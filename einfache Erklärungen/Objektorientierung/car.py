class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.xPosition = 5
        self.yPosition = 5

    def drive(self,x,y):
        self.xPosition += x
        self.yPosition += y

    def print_position(self):
        print("Aktuelle Position Car: x= " + str(self.xPosition) + "| y= " + str(self.yPosition))


car1 = Car()
print(car1.car_brand)
car1.car_brand = "Audi"
car1.horse_power = 2
car1.color = "Red"
print(car1.car_brand)
print(car1.horse_power)
print(car1.color)

car1.print_position()
car1.drive(5,10)
car1.print_position()


