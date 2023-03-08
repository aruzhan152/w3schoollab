f1=open("a.txt", "r")

f2=open("b.txt", "w")

for line in f1:

    f2.write(line)