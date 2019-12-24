import sys
result = []
def celtofah():
    cel = int(input("Enter temperature in celcius"))
    fah = 9/5*cel+32
    result.append((cel,fah))
    print(fah)
def fahtocel():
    fah = int(input("Enter temperature in fahrenheit"))
    cel = 5/9*(fah-32)
    result.append((fah,cel))
    print(cel)
def keltocel():
    kel = int(input("Enter temperature in fahrenheit"))
    cel = kel-273
    result.append((kel,cel))
    print(cel)
def celtokel():
    cel = int(input("Enter temperature in fahrenheit"))
    kel = cel + 273
    result.append((cel,kel))
    print(cel)
def fahtokel():
    fah = int(input("Enter temperature in fahrenheit"))
    kel = 5/9*(fah-32)
    result.append((fah,kel))
    print(kel)
def keltofah():
    fah = int(input("Enter temperature in fahrenheit"))
    cel = 5/9*(fah-32)
    result.append((fah,cel))
    print(cel)


while True:
    print("1.Celcius to Fahrenheit\n")
    print("2.Fahrenheit to Celcius\n")
    print("3.Kelvin to Celcius")
    print("4.Celcius to Kelvin" )
    print("5.Fahrenheit to Kelvin\n")
    print("6.Kelvin to Fahrenheit\n")
    print("8.history")
    i = int(input())
    if(i==1):
        celtofah()
    elif(i==2):
        fahtocel()
    elif(i==3):
        keltocel()
    elif(i==4):
        celtokel()
    elif(i==5):
        fahtokel()
    elif(i==6):
        keltofah()
    elif(i==7):
        print("Thank you")
        sys.exit()
    elif(i==8):
        print(result)