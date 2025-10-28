# #basic function
#
# def greet():
#     print("Hello this is inside the basic greet function")
#
# greet()
#
# #function with parameters
# def add(a,b):
#     return a+b
# result=add(4,6)
# print(result)


#default parameters
def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Ram")

#named arguments
def add(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add(1,2,3,4,5))

#keyword arguments
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
info(name="Sita",age=25,city="Delhi")