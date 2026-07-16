
class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Sleeping")

    def move_fast(self):
        print("Moving: 20km/h")

class Dog(Animal):

    def bark(self):
        print("wau")

class Cat(Animal):

    def purr(self):
        print("schnurr")

class Tiger(Animal):
    def move_fast(self):
        print("Moving: 80km/h")

class Owl(Animal):


    def __init__(self, name, age, color, fav_food, hunting_instinct):
        super().__init__(name, age, color, fav_food)
        self.hunting_instinct = hunting_instinct


    def sleep(self):
        super().sleep()
        print("Gleichgewicht halten")

dog = Dog("Dog", 10, "red", "Fleisch")
dog.sleep()
cat = Cat("Cat", 20, "blue", "Fisch")
print(cat.age)

tiger = Tiger("Tiger", 20, "red", "Fleisch")
dog.move_fast()
tiger.move_fast()
owl = Owl("Eule", 20, "red", "Wurm",7)
owl.sleep()
print(owl.hunting_instinct)

