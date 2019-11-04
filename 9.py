class Student:		
	def __init__(self, name, age, marks):
		self.name = name
		self.age = age
		self.marks = marks

	def accept():
		list = []
		n = input("Enter name of student")
		a = int(input("Enter age"))
		for i in range(3):
			x = int(input("Enter marks of sub " + str(i+1)))
			list.append(x)
		s = Student(n,a,listOfMarks)
		return s

	def display(self):
		print("Name :" + self.name)
		print("Age :" + str(self.age))
		print("Marks :" + str(self.marks))

s1 = Student('Ujuwal',21,[25,21,22])
s1.display()
s2 = Student.accept()
s2.display()
