class Car:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour
    def accelerate(self):
        print("I am accelerating")
    def brake_system(self):
        print("Car is stopping")
c1 = Car("Swift", 1450, "White")
print(c1.name)
print(c1.price)
print(c1.colour)

"""
OUTPUT:

Swift
1450
White


"""
