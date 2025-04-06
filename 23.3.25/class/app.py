from animal_class import *
from vehicle_class import *
try:
    l1 = Lion("simba", "meat")
    e1 = Elephant("dumbo", "mia", 10)
    m1 = Monkey("mimi", "bananas", 30)

    anis = [l1, e1, m1]
    for sound in anis:
        print(sound, end= " ")
        sound.make_sound()
        print()
    
    v1 = Car("infiniti", 4)
    v2 = Bicycle("asaf", True)
    v3 = Airplane("el al", 8)
    vehicle = [v1, v2, v3]
    for a in vehicle:
        print(a, end= " ")
        a.move()
        if isinstance(a, Bicycle):
            print(a.has_basket)
        print()

except Exception as err:
    print(err)