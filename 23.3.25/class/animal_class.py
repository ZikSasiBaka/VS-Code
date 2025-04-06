class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound():
        print("this animal makes a sound")
    
    def __str__(self):
        return f"name: {self.name}"
    
class Lion(Animal):
    def __init__(self, name, eating):
        super().__init__(name)
        self.eating = eating
    
    def make_sound(self):
        print("ROAR, IM A LION!")
    
    def __str__(self):
        return super().__str__() + f" eating: {self.eating}"

class Elephant(Animal):
    def __init__(self, name, eating, tusk):
        super().__init__(name)
        self.eating = eating
        self.tusk = tusk
    
    def make_sound(self):
        print("Trumpet! I am an Elephant")
    
    def __str__(self):
        return super().__str__() + f" eating: {self.eating} tusk: {self.tusk}"

class Monkey(Animal):
    def __init__(self, name, eating, num_bananas):
        super().__init__(name)
        self.eating = eating
        self.num_bananas = num_bananas
    
    def make_sound(self):
        print("ooh ooh ooh im a monkey")

    def __str__(self):
        return super().__str__() + f" eating: {self.eating} num_bananas: {self.num_bananas}"


        