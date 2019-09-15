class Student:
    marks=[]
    def display(self):
        print("Age :"+str(self.age))
        print("Name :"+self.name)
        print("Marks in Physics Chemistry and Math")
        print(*self.marks, sep=' ')

    def accept(self):
        self.name = input("Enter the name of the person")
        self.age = input("Enter his age")
        self.marks.append(int(input("Enter his marks in Physics")))
        self.marks.append(int(input("Enter his marks in Math")))
        self.marks.append(int(input("Enter his marks in Chemistry")))

obj = Student()
obj.accept()
obj.display()
