class Student:
	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks
	def details(self):
		print("\nName : "+ str(self.name) + "\nAge : " +str(self.age)+"\nMarks in English Kannada and Hindi is ")
		print(*self.marks)

	def accept(self):
		self.name = input("Enter name")
		self.age = int(input("Enter age"))
		self.marks = map(int,input("Enter marks").split(" "))

stud = Student("ujwal",12,[12,31,12])
stud.details()
stud.accept()
stud.details()


