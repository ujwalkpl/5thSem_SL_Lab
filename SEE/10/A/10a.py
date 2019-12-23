from functools import reduce
a = list(map(int,input("Enter the list elements").split(" ")))
print(*a)
b = [i*3 for i in a]
print(*b)
sum1 = reduce(lambda x,y:x+y,a)
sum2 = reduce(lambda x,y:x+y,b)
print(sum1)
print(sum2)
