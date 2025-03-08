"""def Add(n1, n2):
    return n1+n2
def Sub(n1, n2):
    return n1-n2
def Multiply(n1, n2):
    return n1*n2
def Divide(n1, n2):
    return n1/n2

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result =calculate(Divide,n1=2,n2=3)
print(result)"""

#nested Function
"""def outer_function():
    print("I'm Outer")

    def inner_function():
        print("I'm Inner")
    inner_function()
outer_function()"""

#Function can be retrned from other function
"""def outer_function():
    print("I'm Outer")

    def inner_function():
        print("I'm Inner")
    return inner_function
Inner_function = outer_function()
Inner_function()"""
import time

#Python Decorator
def Delay_Decorator(function):
    def wrapper_function():
        #Do something before
        time.sleep(2)
        function()
        function()
        # Do something before
    return wrapper_function
@Delay_Decorator
def Say_hello():
    print("Say hello")
Say_hello()

@Delay_Decorator
def Say_bye():
    print("Say bye")
Say_bye()

def Say_greeting():
    print("Say How are you?")
Say_greeting()

