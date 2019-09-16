strr = ["Msrit","sounds","cooler","than","Rit"]
li= [i for i in strr if strr.index(i)%2==0 ]
print(*li,sep = ' ')

b=[strr[x].upper() for x in range(1,len(strr)) if x%3==0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

li2= [i[::-1] for i in strr]

print(*li2,sep = ' ')



print(b) 
