vowels = ["a","e","i","o","u"]
class reverse_string:
    def __init__(self,strr):
        self.strr=strr
    def reverse(self):
        return(' '.join(self.strr.split()[::-1]))

def vowel_count(strr):
    return sum(st in vowels for st in strr.lower())

newlis = []
for i in range(3):
    sen = input("Enter the sentence")
    obj = reverse_string(sen)
    newlis.append(obj)
    print(obj.reverse())

finallis = sorted(newlis,key = lambda x:vowel_count(x.strr),reverse=True)

for x in finallis:
    print(str(x.reverse()) + "  Vowel count :" + str(vowel_count(x.strr)))



