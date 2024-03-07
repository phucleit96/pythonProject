def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 2, 3, 4, 5, 6, 10)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n -= kwargs["subtract"]
    n /= kwargs["divide"]
    print(n)

calculate(2, add=3, multiply=5, subtract=1, divide=2)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
