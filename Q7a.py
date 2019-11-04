 def AtomicDictionary():
	dicti={"sodium":"Na","Hydrogen":"H","Helium":"He","Nitrogen":"N","Lithium":"Li","Boron":"B"}
	print(dicti)
	key=input("Enter a new element")
	value=input("Enter its symbol")
	dicti[key]=value
	print(dicti)
	key=input("Enter a new element")
	value=input("Enter its symbol")
	dicti[key]=value
	print(dicti)
	print("Number of elements in the dictionary is "+str(len(dicti.keys())))
	key=input("Enter an Element")
	print("The atomic symbol is"+str(dicti[key]))

