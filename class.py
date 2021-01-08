#inheritance (self is like this for constructor classes)
class Car():
    """This is a car class that will display the make and model"""
    def __init__(self, make, model, color):
            self.make = make
            self.model = model
            self.color = color
#
        def __str__(self):
            return"{}, {}, {}".format(self.make, self.model, self.color)

    def drive(self):
        self.gas -= 10
        print(self.gas)

    def fill_tank(self):
        self.gas = 100 
        print('Car is now filled')
# F -> like the $ for a javascript ${template literal}
    def check_gas(self):
        print(f"Gas handle: {self.gas}")

car = Car('ferrari', '458', 'white')

car1.drive()
car1.drive()
car1.check_gas()
car1.fill_tan()
car1.check_gas()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Squid():
    def __init__(self, swim, eat, ink):
            self.swim = swim
            self.eat = eat
            self.ink = ink
    def __str__(self):
        return "{}, {}, {}".format(self.swim, self.eat, self.ink)

    def eat(self):
        self.eat = {
            "breakfast": "shrimp",
            "lunch": "squid",
            "snack": "anchovy pizza"
        }

    def ink(self):
        self.ink = {
            "hobby": "ink",
            "lower back tats": "ink",
            "job": "ink"
        }
    
squid1 = Squid("fast", "shrimp", "job")
squid2 = Squid("slow", "anchovy pizza", "hobby")

squid1.eat()
squid1.ink()

squid2.eat()
squid2.ink()
