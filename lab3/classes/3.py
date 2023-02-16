b=int(input())
c=int(input())

class Shape():
    
    def area(self,length,width):
        pass
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=b
        self.width=c
    def area(self):
        a=(self.length*self.width)
        print(a)


cl=Rectangle(b,c)
cl.area()
    
    