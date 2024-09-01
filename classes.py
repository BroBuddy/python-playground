class Car:
    can_drive = True
    num_cars = 0

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_cars += 1

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def offer(self):
        print(f"You offer the {self.color} {self.model}")
        self.for_sale = True

car1 = Car("Mustang", 1976, "black", False)
car2 = Car("Corvette", 1998, "blue", False)
car3 = Car("Viper", 2012, "red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()

print(Car.can_drive)
car2.drive()
car2.stop()
print()

car3.offer()
print(car3.for_sale)
print()

print(Car.num_cars)
