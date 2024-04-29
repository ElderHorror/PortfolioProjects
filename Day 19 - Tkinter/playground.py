def add(*args):
    print(args[0])

    new_n = 0
    for n in args:
        new_n += n
        print(new_n)

add(1,2,3,4,5,6,7,8,9,10,11,12)

def calculate (n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs['multiply']
    print(n)
    # for key, val in kwargs.items():
    #     print(key)
    #     print(val)''

    # print(kwargs["add"])

calculate(2, add=3, multiply=3)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("Color")
        self.sears = kw.get("Seats")


my_car = Car(make="Nissan", model="GT_R")
print(my_car.model)
