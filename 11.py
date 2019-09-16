strr = ["Msrit","sounds","cooler","than","Rit"]
li= [i for i in strr if strr.index(i)%2==0 ]
print(*li,sep = ' ')

print(strr[2].upper())

li2= [i[::-1] for i in strr]

print(*li2,sep = ' ')

 

