def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))

L= [2,4,6,23,1,46]
print(maximum(L))
