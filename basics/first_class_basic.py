import keyword

print(keyword.kwlist)
help(keyword)

#variable name format
snake_case=0
camelCase=1

'''
Indentation 
Statements end without semicolons
Case-sensitive: Variable ≠ variable
Comments: Use # for single-line, triple quotes for multi-line
'''


i=1#int
c='4' #string

a=[1,2,35,6]#list

t=(2,4)#tuple

d={'a':'1'}

#basic conditionals
z=1
if z==1:
    print(z)
elif z!=1:
    print(z)
else:
    print(z)

x=input("enter your value")
# (a + b)  # Addition: 13
# (a - b)  # Subtraction: 7
# (a * b)  # Multiplication: 30
# (a / b)  # Division: 3.3333
# (a // b) # Floor Division: 3
# (a % b)  # Modulus: 1 (Remainder)
# (a ** b) # Exponentiation: 10^3 = 1000