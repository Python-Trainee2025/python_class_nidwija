#
# r = 'car'
# t="apple"
# p = 'race'
# m='madam'
# print(p + r)  # Concatenation
# print(p * 4)  # Repetition
# print(p[1])  # Indexing
# print(t[1:3])  # Slicing [start:end]
# #
# print(m[::-1])  # Reverse string
# #
# print('a' in t)  # Membership test
# print('z' not in t)  # Non-membership test
# print(len(t))  # Length of string
# #
a='Cat '
# i=input("what is the animal type?:: ")
# if i==a:
#     print("yes! correct")
# else:
#     print("incorrect")

print(a.lower())  # Lowercase
print(a.upper())  # Uppercase
print(a.capitalize())  # Capitalize first letter
print(a.title())  # Title Case

z="  fhhdasfi dfhsdfj  "
print(z)
print(z.strip())

print(z.replace("f","X"))

b="hello,my name is ram"
s=b.split(",")
print(s)
o=['hello','hi', 'my name is ram']
j=' ,'.join(o)
print(j)
f="table"
print(f.startswith("t"))
print(f.endswith("e"))
print(f.isalpha())
print(f.count('e'))
