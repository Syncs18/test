
class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Sleeping")

class Dog(Animal):

    def bark(self):
        print("wau")

class Cat(Animal):

    def purr(self):
        print("schnurr")

dog = Dog("Dog", 10, "red", "Fleisch")
dog.sleep()
cat = Cat("Cat", 20, "blue", "Fisch")
print(cat.age)


