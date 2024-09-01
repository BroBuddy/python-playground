class Animal:
    is_alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} makes Woof")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} makes Meow")

dog = Dog("Lea")
cat = Cat("Igor")

dog.eat()
dog.speak()
print()

cat.sleep()
cat.speak()