import math
class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        print(math.pi*self.radius*self.radius)
circle(int(input("Enter the number"))).area()
