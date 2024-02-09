class Shape:
    def area(self):
        print("0")


class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self,length):
        print(self.length**2)
        
square = Square(6)
square.area(6)