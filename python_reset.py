#module import
import time as t

#variable assignment
x= "James"
y= "Sully"
y= "Jackson" #Variable reassignment 

print(x, y) #this prints out the value stored in variables x and y
            #the comma automatically creates a space between each value it separates
            #print(x y): this would give an error because x and y aren't seperated with the right syntax rules

#String concatenation using , and +
""""""
print("Hello""World") #Displays: HelloWorld
print("Hello","World") #Displays: Hello World
print("Hello" + "World") #Displays: HelloWorld
print("Hello " + "World") #Displays: Hello World
print("Hello","World") #Displays: Hello World
#take note of the differences used in displaying the output Hello World

"""
* print() is used to display information to the console.
* print(), by default, has an end line character \n (it is an escape sequence ). This causes the cursor to go to a new line after the output is displayed.
* end= is an optional paramter that can be used to explicitly control what the end character is. It determines the character(s) appended to the end of the output. 
* By default, end is set to \n
"""

#print(f"Hello World {end='!'}")
"""
The code above will cause an error because end= is a function parameter and is seperate argument from the string (should be seperated by a comma)
Putting it inside the string makes Python see it as a part of the string
It will look for a variable name end= and eventually cause a syntax error since it doesn't exist

print("Hello World", end="!")
#     ^--Arg 1--^    ^--Arg 2--^
"""

# INPUT
# The input() function collects/reads data from the user and returns a string to a called variable.
# It returns a string. Data type conversion is used to change data types from one form to another.

#Simple interactive program without input validation
name= input("Enter your name: ")
age= int(input("Enter your age: "))
gpa= float(input("Enter your CGPA: "))

t.sleep(0.5)
print(f"Hello, {name}. Nice to meet you! \n"
      f"Next year you'll be {age+1}")

t.sleep(0.5)
if gpa >= 3.0:
    print(f"Great job getting a {gpa} gpa")
else:
    print("Great job. You have great potential for something better!")

#DATA TYPE CONVERSION
"""
str()
float()
int()

Conversion on float to an int causes truncation of the fractional part (meaning no rounding)
"""

#SIMPLE OPERATORS
"""
/: Used for floating point division; it always returns a float.
//: Used integer or floor division; +ve answers are truncated and negative answers are rounded down (toward -ve infinity).
**: Used for exponentiation. The operand on the left of ** is the base, and the operand on the right is the power
%: Used for modulus or remainder division.

ORDER OF OPERATION:
Parentheses ()
Exponentiation **
Multiplication * , Division / , Floor Division // , Remainder %
Addition + , Subtraction -
"""
