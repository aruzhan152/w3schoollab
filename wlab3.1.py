# 1
class myClass:
    def getString(self):
        n = str(input("Input a string: "))
        return n
    def printString(self, string):
        print(string.upper())

a = myClass()
string = a.getString()
a.printString(string)

# 2
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
        
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length**2
sh1 = Shape()
sq1 = Square(2)
print(sq1.area())
print(sh1.area())

# 3
class Rectangle (Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
re1 = Rectangle(2, 4)
print(re1.area())

#4
from math import *
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("x: ", self.x, "y: ", self.y)
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
    def dist(self, obj):
        return sqrt((self.x-obj.x)**2+(self.y-obj.y)**2)
p1 = Point(2, 4)
p2 = Point(-3, 1)
print(p1.dist(p2))

# 5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Not enough money!")

acc1 = Account("Jack", 100)
print(acc1.balance)
acc1.deposit(30)
print(acc1.balance)
acc1.withdraw(70)
print(acc1.balance)
acc1.withdraw(100)

#6
def prime(ls):
    return list(filter(lambda x: all(x%i != 0 for i in range(2,int(x**0.5)+1)) and x != 1, ls))

l = [1,2,3,4,5,6,7,8,9]
print(prime(l))