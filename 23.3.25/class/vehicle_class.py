class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"{self.brand}"
    
    def move(self):
        print("the vehicle is moving")
    
class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

    def move(self):
        print("the car drives on the road")

class Bicycle(Vehicle):
    def __init__(self, brand, has_basket):
        super().__init__(brand)
        self.has_basket = has_basket
    
    def has_basket(self):
        return self.has_basket
    
    def move(self):
        print("the bicycle is pedaling on the path")

class Airplane(Vehicle):
    def __init__(self, brand, engine_count):
        super().__init__(brand)
        self.engine_count = engine_count
    
    def move(self):
        print("the airplane flies in the sky")