studentdir = { 1:'Ujwal',2:'Uzma',3:'Vaibhav',4:'Vishwa'}

a=[studentdir[i] for i in studentdir if i%2==0]

print(*a,sep=' ')
