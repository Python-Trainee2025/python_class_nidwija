'''
LEGB
Rule(Local → Enclosing → Global → Built - in)
Local (L) → Inside the current function.
Enclosing (E) → Inside enclosing functions (nested functions).
Global (G) → Defined at the top level of a script/module.
Built-in (B) → Predefined Python functions (like print, len).

'''


x = 10  # Global scope

def outer():
    x = 5  # Enclosing scope
    def inner():
        x = 1  # Local scope
        print("Inner:", x)  # Uses local x
    inner()
    print("Outer:", x)      # Uses enclosing x

outer()
print("Global:", x)         # Uses global x