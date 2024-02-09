import math
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print("coordinates of the point is ", self.x,",",self.y)
    def move(self,q,w):
        self.x = q
        self.y = w 
    def dist(self,x1,y1):
        print("the distanse of 2 points is " , math.sqrt((x1-self.x)**2+(y1-self.y)**2))

point1 = point(5,6)
point1.dist(10,11)

