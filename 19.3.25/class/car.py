# object is instance (מופע) of class (תבנית)
# static property belongs to class (תבנית)
class Car:
    # constructor:
    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price
    
    # functions:
    def display(self):
        print(f"{self.color} {self.model} {self.__price}")
    
    def __str__(self):
        return (f"color: {self.color} model: {self.model} price: {self.price}")

    @property
    def price(self):
        return self.__price
    
    # setters and getters:
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price has to be positive")
        else:
            self.__price = value

try:
    car1 = Car("black", "qx55", 400000)
    car1.price = -400000
    print(car1)

except Exception as err:
    print(err)










