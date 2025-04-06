class Flashlight:
    counter = 0
    def __init__(self, color, length, light_power,num_of_batterys):
        self.color = color
        self.length = length
        self.light_power = light_power
        self.num_of_batterys = num_of_batterys
        Flashlight.counter += 1

    def on(self):
        print("flashlight is on")
    
    def off(self):
        print("flashlight is off")
    
    def battery_switch(self):
        print("batterys have been replaced")

    def display(self):
        print(f"{self.color} {self.__length} {self.light_power} {self.num_of_batterys}")
    
    def __str__(self):
        return f"color: {self.color}, length: {self.__length}, light power: {self.light_power}, number of battery's: {self.num_of_batterys}"

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, int):
            raise ValueError("length of flashlight has to be between 10cm to 30cm")
        else:
            self.__length = value
    
    @property
    def light_power(self):
        return self.__light_power
    
    @light_power.setter
    def light_power(self, value):
        if not isinstance(value, int):
            raise ValueError("light power has to be from 0 - 5")
        else:
            self.__light_power = value

    @staticmethod
    def show_counter():
        print(Flashlight.counter)


try:
    f1 = Flashlight("black", 10, 0, 3)
    f1.length = 25
    f1.light_power = 4
    f1.on()
    f1.off()
    f1.battery_switch()
    print(f1)

except Exception as err:
    print(err)

        