class Rectangle:
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth

newRec = Rectangle(4,5)
print(newRec.area())
