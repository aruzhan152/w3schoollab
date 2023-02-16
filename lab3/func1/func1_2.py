def Convert(Fahrenheit):
    celsius = (5 / 9) * (Fahrenheit - 32)
    return celsius
Fahrenheit=float(input("Enter in Fahrenheit: "))
cn=Convert(Fahrenheit)
print(cn)