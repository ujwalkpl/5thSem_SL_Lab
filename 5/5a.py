import cmath
a=list(map(float,input("Enter the value of A B and C").split(" ")))
print(-a[1]/(2*a[0])+cmath.sqrt((a[1]**2-4*a[0]*a[2])/(2*a[0])))
print(-a[1]/(2*a[0])+cmath.sqrt((a[1]**2+4*a[0]*a[2])/(2*a[0])))



