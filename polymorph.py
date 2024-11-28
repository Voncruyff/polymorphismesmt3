class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def sound(self):
        return "Cat meows"

def animal_sound(animal):
    print(animal.sound())

# Penggunaan
my_dog = Dog()
my_cat = Cat()

animal_sound(my_dog)  # Output: Dog barks
animal_sound(my_cat)   # Output: Cat meows