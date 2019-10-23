tuplelist = []
def celcius_to_fahrenheit():
    celsius = int(input("Enter temperature in celcius"));
    fahrenheit = 9/5*celsius+32;
    tuplelist.append((celsius,fahrenheit))
    print("Temperatur in  Fahrenheit is " + str(fahrenheit));

def fahrenheit_to_celsius():
    fahreheit = int(input("Enter temperature in fahrenheit"));
    celsius = (fahreheit-32)*5/9
    tuplelist.append((fahreheit,celsius))
    print("Temperature in celsius is " + str(celcius));

def kelvin_to_celsius():
    kelvin = int(input("Enter temperature in kelvin"));
    celsius = kelvin-273.15
    tuplelist.append((kelvin,celsius))
    print("Temperature in celsius is " + str(celsius));

def celsius_to_kelvin():
    celsius = int(input("Enter temperature in celsius"));
    kelvin = celsius + 273.15
    tuplelist.append((celsius,kelvin))
    print("Temperature in Celsius is " + str(kelvin))

def fahrenheit_to_kelvin():
    fahrenheit = int(input("Enter temperature in fahrenheit"))
    kelvin = (fahrenheit-32)*5/9+273.15
    tuplelist.append((fahrenheit,kelvin))
    print("Temperature in Kelvin is " + str(kelvin))

def kelvin_to_fahrenheit():
    kelvin = int(input("Enter temperature in kelvin"))
    fahrenheit = (kelvin-273.15)*9/5+32
    tuplelist.append((kelvin,fahrenheit))
    print("Temperature in fahrenheit is "+ str(fahrenheit))

print("Enter Choice\n1.celsius to fahrenheit\n2.fahrenheit to celsius\n3.kelvin to celsius\n4.celsius to kelvin\n5.fahrenheit to kelvin\n6.kelvin to fahrenheit\n7.exit")
choice=0
while(choice!=7):
    choice=int(input())
    if(choice==1):
        celcius_to_fahrenheit()
    elif(choice==2):
        fahrenheit_to_celsius()
    elif(choice==3):
        kelvin_to_celsius()
    elif(choice==4):
        celsius_to_kelvin()
    elif(choice==5):
        fahrenheit_to_kelvin()
    elif(choice==6):
        kelvin_to_fahrenheit()
print(tuplelist)
print("Thank you")