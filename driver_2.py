class Novice_Driver:
    # def __init__(self,name,age,license,speed):
    #     self.name=name
    #     self.age=age
    #     self.license=dr_license_2
    #     self.speed = speed

    def drive(self):
        print(f"This driver`s license code is {self.dr_license_2}")


import random

speed_list=[0]
for speed in speed_list:
    speed_list.append(random.randint(0,300))
    if 60<speed<90:
        print(speed)
        print("stop")
        print(speed_list)
        break


person_2 = input("Name and surname of second driver:\t")
person_2_age = int(input("Input age of second driver:\t"))
dr_license_2 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))