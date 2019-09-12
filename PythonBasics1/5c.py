i=0
j=1
n=int(input("the no of digits in fibonacci"))
if n==0:
	print(0)
elif n==1:
	print(0)
elif n>=2:
	print(i)
	print(j)
for n in range(2,n):
	k=i+j
	print(k)
	i=j
	j=k
