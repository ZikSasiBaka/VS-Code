class Speaker:
    counter = 0
    def __init__(self, designer, model, color, volume):
        self.designer = designer
        self.model = model
        self.color = color
        self.volume = volume
    
    def display(self):
        return(f"{self.designer} {self.model} {self.color} {self.__volume}")
    
    def __str__(self):
        return (f"designer: {self.designer}, model: {self.model}, color: {self.color}, volume: {self.__volume}")
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        if value < 0 or value > 100:
            raise ValueError("volume has to be higher than or equal to 0")
        else:
            self.__volume = value
    
    @staticmethod
    def show_counter():
        print(Speaker.counter)
        

try:
    speaker1 = Speaker("JBL", "Flip6", "Dark", 60)
    print(speaker1)

except Exception as err:
    print(err)


        