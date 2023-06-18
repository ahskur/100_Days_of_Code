def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,3,5,7,76,7,5,23,6))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car():
    def __init__(self, **kwargs):
        # You can use .get to get the argument, but if isn't there, the program doesn't crash
        # but if using just kwargs["make"] for example, if the argument isn't present, the program crashes
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make= "Nissan", model= "GT-R")
print(my_car.model)