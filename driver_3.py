class Experienced_Driver:
    def drive(self):
        print(f"This driver`s license code is {self.dr_license_3}")

        import random

    speed_list = [0]
    random_number=random.randint(0,300)
    for speed in speed_list:
        speed_list.append(random.randint(0, 300))
        if (person_3_age+speed)/2==random_number:
            print("The police stopped")



person_3 = input("Name and surname of third driver:\t")
person_3_age = int(input("Input age of third driver:\t"))
dr_license_3 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))