class Shape():
    area=0
    def area(self,length):
        pass
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        a=(self.length*self.length)
        print(a)
        
cl=Square(15)
cl.area()
