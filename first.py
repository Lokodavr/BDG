person_1 = input("Name and surname of first driver:\t")
person_2 = input("Name and surname of second driver:\t")
person_3 = input("Name and surname of third driver:\t")
person_1_age = int(input("Input age of first driver:\t"))
person_2_age = int(input("Input age of second driver:\t"))
person_3_age = int(input("Input age of third driver:\t"))
dr_license_1 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))
dr_license_2 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))
dr_license_3 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))
p_1 = {person_1: person_1_age}
p_2 = {person_2: person_2_age}
p_3 = {person_3: person_3_age}

length_of_list = 3
my_list_of_drivers = []
while len(my_list_of_drivers) < length_of_list:
    if dr_license_1 == 1 and dr_license_2 == 1 and dr_license_3 == 0:
        my_list_of_drivers.append(p_1)
        my_list_of_drivers.append(p_2)
        my_list_of_drivers.append(p_3)
    else:
        person_1 = input("Name and surname of first driver:\t")
        person_2 = input("Name and surname of second driver:\t")
        person_3 = input("Name and surname of third driver:\t")
        person_1_age = int(input("Input age of first driver:\t"))
        person_2_age = int(input("Input age of second driver:\t"))
        person_3_age = int(input("Input age of third driver:\t"))
        dr_license_1 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))
        dr_license_2 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))
        dr_license_3 = int(input("Have license - YES OR NO:type answer 1 for yes or 0 for no:\t"))

print(my_list_of_drivers)

# my_list_of_drivers = []
# if dr_license_1 == 1:
#     my_list_of_drivers.append(p_1)
# elif dr_license_2==1:
#     my_list_of_drivers.append(p_2)
# elif dr_license_3==0:
#     my_list_of_drivers.append(p_3)
# else:
#     print ("Please try again")

# print(my_list_of_drivers)

# print(p_1)
# print(p_2)
# print(p_3)
