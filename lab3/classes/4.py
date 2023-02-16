from math import sqrt
x=int(input())
y=int(input())
class Point():
    def __init__(self,point1,point2):
        self.point1=x 
        self.point2=y
        
    def Show(self):
        print(self.point1,self.point2)
    def Move(self):
        x1=int(input())
        y1=int(input())
        self.point1=x1 
        self.point2=y1
    def Dist(self):
        dist=sqrt(pow(self.point1,2)+pow(self.point2,2))
        print(dist)
        
cl=Point(x,y)
cl.Dist()
cl.Show()
cl.Move()
        
        