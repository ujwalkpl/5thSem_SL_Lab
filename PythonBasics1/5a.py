a=int(input("marks in math"))
b=int(input("marks in physics"))
c=int(input("Marks in chemistry"))

s=a+b+c

if a>=65 and b>=55 and c>=50 and s>=180:
	flag=1
else:
	flag=0
if flag==1:
	print("Eligibility",bool(flag))
else:
	print("Eligibility",bool(flag))


