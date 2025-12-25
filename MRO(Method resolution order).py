class Alpha:
    def fun(self):
        print("I am an Alpha")
class Beta:
    def fun(self):
        print("I am Beta")
class Gamma(Alpha, Beta):
    pass
g = Gamma()
g.fun()


"""
OUTPUT:

I am an Alpha

"""
