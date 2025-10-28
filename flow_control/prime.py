n=int(input("enter a number: "))
p=True

if n<2:
    p=False
else:
    for i in range(2,n):
        if n%i==0:
            p=False
            break
print(f'is prime? {p}')