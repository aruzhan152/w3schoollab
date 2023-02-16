def Convert(ounce):
    gram=(ounce/28.35)
    return gram
ounce=float(input("enter in ounce: "))
cn=Convert(ounce)
print(cn)