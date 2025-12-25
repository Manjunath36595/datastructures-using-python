class Alpha:
    def fun(self):
        print("I am an Alpha")
class Beta(Alpha):
    def fun(self):
        print("I am Beta")
class Gamma(Beta):
    def fun(self):
        print("I am Gamma")
g = Gamma()
g.fun()


"""
OUTPUT:

I am Gamma



"""
