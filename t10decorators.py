# A decorator allows to insert logic before and after the function is called.
#
# To create one, define a function that that a function
# as input and returns a function as output.
def identity(func):
    print("Identity wrapper!")
    return func


@identity
def add(x, y):
    return x + y


# Parametrised decorator.
def parametrised_identity(p):
    def f(func):
        print(p)
        return func

    return f


@parametrised_identity("PARAMETRISED!")
def subtract(x, y):
    return x - y


# You can use class decorators to modify classes dynamically.
def add_chirp(cls):
    """ Class decorator to add chirp method. """

    def chirp(self):
        return "CHIRP"

    cls.speak = chirp
    return cls


@add_chirp
class Bird:
    pass


b = Bird()
print(b.speak())


def howl(self):
    return "HOWL"


def creating_classes_with_type():
    parents = ()
    attrs_map = {'speak': howl}
    F = type('F', parents, attrs_map)

    f = F()
    print(f.speak())


creating_classes_with_type()


# Metaclasses with Functions.
def meta(name, parents, attrs_map):
    def bark(self):
        return "WOOF!"

    attrs_map['speak'] = bark
    return type(name, parents, attrs_map)


class Dog(metaclass=meta):
    pass


d = Dog()
print(d.speak())


# Class decorator. Must inherit from type.
# Either __new__ or __init__ can be used for modification,
# but __new__ is more flexible.
class CatMeta(type):
    def __new__(cls, name, parents, attrs_map):
        # cls is CatMeta
        # res is the class we are creating
        res = super().__new__(cls, name, parents, attrs_map)

        def meow(self):
            return "Meow"

        res.speak = meow
        return res

    def __init__(cls, name, parents, attrs_map):
        super().__init__(name, parents, attrs_map)


class Cat(metaclass=CatMeta):
    pass


c = Cat()
print(c.speak())
