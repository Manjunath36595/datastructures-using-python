class Alpha:
    pass
class Beta(Alpha):
    pass
class Gamma(Beta):
    pass
print(Gamma.mro())


"""
____OUTPUT___

[<class '__main__.Gamma'>, <class '__main__.Beta'>, <class '__main__.Alpha'>, <class 'object'>]

"""
