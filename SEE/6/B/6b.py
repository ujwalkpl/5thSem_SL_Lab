vowels = ['a','e','i','o','u']
class stringreverse:
    def __init__(self,sentence):
        self.sentence = sentence
        self.reverse = " ".join(reversed(self.sentence.split()))
        self.vowelcount = sum([ i in vowels for i in self.sentence.lower()])
    
str1 = stringreverse("ujwal is a good boy")
print(str1.reverse)
print(str1.vowelcount)

result = []
for i in range(3):
    obj = stringreverse(input("Enter a string"))
    result.append(obj)
    print(obj.reverse)
strfinal = sorted(result,key = lambda x:x.vowelcount,reverse = True)
for i in strfinal :
    print(str(i.reverse) + " " + str(i.vowelcount))