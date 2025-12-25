class Car:
    def __init__(self):
        self.name = "Swift"
        self.price = 2345678
        self.colour = "Blue"
    def accelerate(self):
        print("I am accelerating")
        print(self.colour)
    def brake_system(self):
        print("Car is stopping")
    def start(self):
        print("Car is starting")
c1 = Car()
c1.start()
c1.accelerate()
c1.brake_system()


"""

OUTPUT:

Car is starting
I am accelerating
Blue
Car is stopping


"""
