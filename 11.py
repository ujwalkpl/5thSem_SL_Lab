strr = ["Msrit","sounds","cooler","than","Rit","heyvishwa123"]
print(strr[::2])

b=[strr[x].upper() for x in range(1,len(strr)) if (x+1)%3==0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

li2= [i[::-1] for i in strr]
print(*li2,sep = ' ')
print(b) 


for elem in strr:
	print(elem)
	res = [int(i) for i in elem if i.isdigit()] 
	print(res)
