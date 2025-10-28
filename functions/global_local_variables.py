#
# def func():
#     x = 10  # Local variable
#     print(x)
#
# func()


# x = 5  # Global variable
#
# def func():
#     print(x)
#
# func()


# x = 5  # Global variable
# print("Before modify:", x)
#
# def modify():
#     global x
#     x = 10  # Modifies the global variable
#     print("Inside modify:", x)
#
# modify()
# print("After modify:", x)


def outer():
    x = 5  # Enclosing variable
    print("Before inner:", x)

    def inner():
        nonlocal x
        x = 10  # Modifies the enclosing variable
        print("Inside inner:", x)

    inner()
    print("After inner:", x)


outer()
