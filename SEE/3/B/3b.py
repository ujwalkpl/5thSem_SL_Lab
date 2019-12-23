import sys
import os
from functools import reduce
if(len(sys.argv)!=2):
    print("arguments are not correct")
    sys.exit()

if(sys.argv[1].split(".")[1]!="txt"):
    print("file should be a text file")
    sys.exit()
if(not os.path.exists(sys.argv[1])):
    print("File not found")
    sys.exit()

wordnet = {}
with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
            wordnet[word] = wordnet.get(word,0)+1

print(wordnet)

newlist = sorted(wordnet.items(),key = lambda x:x[1],reverse = True)

print(newlist[:10])
lenlist = []

for i in range(len(wordnet)):
    lenlist.append(newlist[i][1])
print(lenlist)
sum = reduce(lambda x,y:x+y,lenlist)
print(sum/len(wordnet))

oddans = [i**2 for i in lenlist if i%2!=0]
print(oddans)





