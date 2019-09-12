num=int(input("Enter the number"))

def primeis(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag):
        print("NOt a Prime")
    else:
        print("Prime")
primeis(num)

            
