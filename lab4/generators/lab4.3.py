def div(x):
    i=1
    while i<x:
        if i%3==0 or i%4==0:
            yield i
        i=i+1

b=int(input())
for i in div(b):
    print(i)

