def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(3, 5, 6, 15, 33, 45)

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=6, multiply=8, uyfuy=67)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="Gt-R")
print(my_car.model)
