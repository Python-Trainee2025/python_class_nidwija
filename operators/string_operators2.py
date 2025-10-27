p = 'car'
r = 'race'

# split/join
b = 'hello,my,name'
print(b.split(','))  # Split into a list

o = ['hello', 'hi']
print(','.join(o))  # Join with a separator

print(p.startswith('c'))  # Starts with 'c'
print(r.endswith('e'))  # Ends with 'e'
print(p.isalpha())
print('123'.isdigit())
print('   '.isspace())
print(p.isalnum())
print(r.count('a'))
