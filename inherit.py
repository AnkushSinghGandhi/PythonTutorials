class Animal:
    def speak(self):
        print("animal speaking")
#dog inherits the base class animal
class Dog:
    def bark(self):
        print("dog barking")
class Sandeep(Dog,Animal):
    def cries(self):
        print("suusu is crying")

d= Sandeep()
d.bark()
d.speak()
d.cries()