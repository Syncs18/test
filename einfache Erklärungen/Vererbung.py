
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

#Mehrfach vererbung

class Person:
    def __init__(self, fname, nname, age):
        self.fname = fname
        self.nname = nname
        self.age = age

    def print_details(self):
        print(self.fname + " " + self.nname + " " + self.age)

class Employee:
    def __init__(self, nname, id):
        self.nname = nname
        self.id = id

    def print_details(self):
        print("Mitarbeiter=" +self.nname + ", id=" + str(self.id))

class Teacher(Person, Employee):
    def __init__(self, fnamen, nname, age, id):
        Person.__init__(self,fnamen,nname,age)
        Employee.__init__(self,nname,id)



teacher = Teacher("Max", "Mustermann", 31, 12)
print(teacher.fname)

#Klassenattribute

class Person2:
    counter = 0

    def __init__(self, fname, nname, age):
        self.fname = fname
        self.nname = nname
        self.age = age
        Person2.counter += 1

    def print_details(self):
        print(self.fname + " " + self.nname + " " + self.age)

p1 = Person2( "Max", "Mustermann", 31)
p2 = Person2( "Ma", "Muster", 30)
print(p1.counter)
print(Person2.counter)

# Statische Methoden

class Math:
    @staticmethod
    def multiply ( a,b):
        return a*b


print(Math.multiply(2,3))

import math

class Circle:
    counter = 0
    def __init__(self, radius):
        self.radius = radius
        Circle.counter += 1
    def area(self):
        return math.pi * self.radius**2
    @staticmethod
    def convert_area_in_radius(area):
        return math.sqrt(area/math.pi)
    @classmethod
    def from_area(cls, area):
        r = math.sqrt(area / math.pi)
        return cls(r)

    @classmethod
    def print_counter(cls):
        print(Circle.counter)

class Rim(Circle):
    pass



c=Circle(3)
c2 = Circle(Circle.convert_area_in_radius(80))
print(c2.area())
Circle.print_counter()

print(Circle.convert_area_in_radius(c.area()))
c3 = Circle.from_area(70)
print(c3.area())
rim = Rim.from_area(20)


# Property Attribute

class Circle2:
    counter = 0
    def __init__(self, radius):
        self._radius = radius
        Circle.counter += 1
    def area(self):
        return math.pi * self._radius**2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,radius):
        if radius >= 0:
            self._radius = radius

    def __len__(self):
        return self._radius

    def __str__(self):
        return "Circle(radius=" + str(self._radius) + ")"

    def __call__(self):
        print("eine instanz kann als funktion aufgerufen werden")

    #def get_radius(self):
     #   return self._radius

    #def set_radius(self, radius):
      #  if radius>=0:
      #      self._radius = radius


i = Circle2(3)
print(i.area())
print(i.radius)
i.radius = 10

test_list = [1,3,5,6]
print(len(i))
print(i)
i()



