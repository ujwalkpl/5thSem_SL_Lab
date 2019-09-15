import functools
lis=[12,2,3,45,5,5]
bis=[x*3 for x in lis]
print("First list is"+str(lis))
print("Second list is"+str(bis))

print("The sum of the elements of the first list is"+str(functools.reduce(lambda x,y:x+y,lis)))
print("The sum of the elements of the second list is "+str(functools.reduce(lambda x,y:x+y,bis)))
