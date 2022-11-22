from first import *
from driver_1 import *
from driver_2 import *
from driver_3 import *

class Drivers:
    def __init__(self, name, age,license,speed):
        self.name = name
        self.age = age
        self.license=license
        self.speed=speed

class No_License(Drivers):
    def __init__(self, name, age, license,speed):
        super().__init__(name,age)
        self.license = dr_license_1
        self.speed=speed

    def displayp_1(self):
        print("Driver`s name:", self.name)


class Novice_Driver(Drivers):
    def __init__(self):
        self.license=dr_license_2
        self.speed=speed

class Experienced_Driver(Drivers):
    def __init__(self):
        self.license=dr_license_3
        self.speed=speed

# A = Drivers("person_1", person_1_age)
# A.display()