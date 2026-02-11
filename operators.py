# comparison operators compare two values and return true or false
"""
Python uses things like and, or, is, in, is not, not in, not etc.
not negates final boolean output

x = 7
x += 3
print(x >= 3)
print(x)
"a" in "apple"
letters= ["a", "b", "c"]
print("B" in letters)

letters= ["a", "b", "c"]
print("B" not in letters)

print (len("jack") is len("jill"))

print( 3>2 and 4<5 )
print( 3<2 and 4<5 )
print( 3<2 or 4<5 )

print(False)
print(not False)
print(not not False)
"""

#EXERCISES
#1-4
age = 18
height = 5.6
comPlex = 1 + 3j
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area= 0.5 * base * height
print(area, "unit ^2")

#5
print("Enter sides a, b and c of your triangle below: ")
a = int("Enter value of a: ")
b = int("Enter value of b: ")
c = int("Enter value of c: ")
print("perimeter: ", a+b+c)

#6-7 (skipped)

#8
print("Equation: y = 2x - 2")
print("y-intercept:", 2*0 - 2)
print(f"x-itercept:" {(0-2)/2}"")
print("slope is m in y= mx +b: 2")


#9 & 10
import math 
y1 = 2
y2 = 10
x1 = 2
x2 = 6
m = (y2 - y1)/(x2 - x1)
print("slope:", m)
#euclidean distance= sqrt((x2-x1)^2 + (y2-y1)^2)
eclu_dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"euclidean distance: {eclu_dist:.0f} units")

#11
x = -3
y = x**2 + 6*x + 9
print(y)

#12: make false statement
py = len("python")
drag = len ("dragon")
print(py > drag)

#OR
print(len("python") > len ("dragon"))
print(py < drag)
print(py != drag)

#13
#wrong: 
check = 'on' in 'python' and 'dragon'
print(check)


#In Python, the and operator returns the first value if it is "falsy." 
#If the first value is "truthy" (like True), it returns the second value.
#Result: Since True is truthy, Python returns the second part of the comparison: 'dragon'.

#correct:
check = 'on' in 'python' and 'on' in 'dragon'
print(check)

#14
text = "I hope this course is not full of jargon"
checker = "jargon" in text
print(f"Is \"jargon\" inside the text?: {checker}")

#15-skipped

#16
length = len("python")

float_length = float(length)

string_length = str(float_length)

print(f"int_length:  {type(length)}; {length}")
print(f"float_length:  {type(float_length)}; {float_length}")
print(f"string_length:  {type(string_length)}; {string_length}")

#17
num = int(input(("Enter a number: ")))

if num % 2 == 0:
    print("The number you have entered is even")
else:
    print("The number you have entered is odd")
 
#18 
data= 7//3 == int(2.7)
print("7//3 == int(2.7)")
print(f"The data is: {data}")

#19
print(type('10') is type(10))

#20
try:
    if (int('9.8') == 10):
        print("Data is true")
except :
    print("Data is false")

#21 -skipped

#22
years = int(input("Enter your age: "))

time_lived = years * 365 * 24 * 60 * 60

print(f"You have lived for approximately {time_lived:,} seconds")
#note :, serves as a thousands separator in f-string formatting
#:.2f is for decimal/floating points

#23
for num in range(1,6):
    print(num, end="\t")
    print(third := num//num, end="\t")
    print(fourth := third * num, end="\t")
    print(fifth := fourth * num, end="\t")
    print(fifth * num)

#OR

for n in range(1,6):
    print(f"{n} \t 1 \t {n} \t {n**2}\t {n**3}")

#OR


for n in range(1,6):
    print(f"{n:<3}{1:<3}{n:<3}{n**2:<4}{n**3}")
