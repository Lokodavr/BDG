class No_License:
    # def __init__(self,name,age,license,speed):
    #     self.name=name
    #     self.age=age
    #     self.license=license
    #     self.speed=speed

    def drive(self,dr_license_1):
        print(f"This driver`s license code is {self.dr_license_1}")

    import random

    speed_list = [0]
    for speed in speed_list:
        speed_list.append(random.randint(0, 300))
        if speed > 60:
            print(speed)
            print("stop")
            print(speed_list)
            break

person_1 = input("Name and surname of first driver:\t")
person_1_age = int(input("Input age of first driver:\t"))
dr_license_1 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))
info_list=[person_1,person_1_age,dr_license_1]


voditel=No_License("person_1",person_1_age,dr_license_1)
print(voditel)
