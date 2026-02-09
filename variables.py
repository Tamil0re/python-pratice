#Day 2: 30 Days of python programming Exercise by Asabeneh

#LEVEL 1
#no. 1-13
firstName = "Oluwatamilore"
lastName = "Bamidele-Sanni"
full_name = "Oluwatamilore Bamidele-Sanni"
country = "Nigeria"
city = "Lagos"
age= 18
year= 2026
is_married = False
is_true = "Christian"
is_light_on = True
x, y, z = 12, 36, 48

#LEVEL 2
#1.
print(f"First Name is: {type(firstName)}")
print(f"Last Name is: {type(lastName)}")
print(f"Country is: {type(country)}")
print(f"City is: {type(city)}")
print(f"Age is: {type(age)}")
print(f"Year is: {type(year)}")
print(f"is_married is: {type(is_married)}")
print(f"is_true is: {type(is_true)}")
print(f"is_light_on is: {type(is_light_on)}")

#2.
print(f"My name is {len(firstName)} character(S) long")

#3.
if len(firstName) > len(lastName):
    print("Your first name has a greater no. of characters than your last name.")
elif len(firstName) == len(lastName):
    print("Your first and last name have equal no. of characters.")
else:
    print("Your last name has a greater no. of characters than your first name.")

#4.
num_one = 5
num_two = 4

#5. to 11.
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#12.
import math as m
radius= 30
area_of_circle = m.pi * m.pow(radius, 2)
circum_of_circle = 2 * m.pi * radius

print(f"Area: {area_of_circle:.0f}")
print(f"Circumference: {circum_of_circle:.0f}")

new_radius= int(input("Enter an integer radius: "))
area_of_circle = m.pi * m.pow(new_radius, 2)
print(f"Area: {area_of_circle:.0f}")

#13.
firstName = input("Enter your firstname: ")
lastName = input("Enter your lastname: ")

country = input("Enter the name of your country: ")
age = int(input("Enter your age: "))
