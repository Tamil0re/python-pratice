#ITERABLE TYPE  
'''
print(type("Mohammed")) #string
print(type({"banana", "mango", "apple"})) #set {}
print(type({1:"banana", 2:"mango" , 3: "apple"})) #dictionary {x:y,...}
print(type(["banana", "mango", "apple"])) #list []
print(type(("banana", "mango", "apple"))) #tuple ()
print(type(set(("banana", "mango", "apple")))) #set using set constructor and parenthesis
'''

#end= 
'''
print("One", end='')
print("Two", end='')
print("Three")
'''

#BUILT-IN FUNCTION
"""
number= {1: "one", 2: "two", 3: "three"}
print(len(number)) # counts the 3 mappings within this dictionary

number= [2, 15, 14, 9, -29, 15.000001]
print(max(number)) # checks for the highest value = 15.000001

number= [-2, -15, -14, -9, -29, -15.000001, False]
print(max(number)) # checks for the highest value = False 
#(bool are treated as 1 and 0 under the hood, 0 or false is the highest in the list )

strings= ["a", "b", "x", "e", "f", "zoo"] 
print(max(strings)) #compares the strings using their unicode(ASCII) values

#lists on which max() is used cannot contain a mixture of strings and numbers, it's either/or.

name= "Tami Sanni"
print(tuple(name)) #('T', 'a', 'm', 'i', ' ', 'S', 'a', 'n', 'n', 'i')

name= "Tami Sanni"
print(list(name)) ['T', 'a', 'm', 'i', ' ', 'S', 'a', 'n', 'n', 'i']
"""

#Argument: Item passed into a function
