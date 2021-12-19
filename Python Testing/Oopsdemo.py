# classes are user defined blueprint or prototype
# sum,multiplication,addition,constant
# methods, class variable,instance variables, constructor etc
# object for your classes
# self keyword is mandatory for calling variable name into method
# instance and class variables have whole different purpose
# constructor name should be _init_
# new keyword is not required when you create object


class Calculator:
    num = 100 # class variable
    # default constructor, same as method

    def __init__(self, a, b):
        self.firstNumber = a # instance variable
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now execution as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num
obj = Calculator(2, 3) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj = Calculator(4, 5) #syntax to create objects in python
obj.getData()
print(obj.Summation())

