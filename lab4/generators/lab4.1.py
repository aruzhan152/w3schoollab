def sqr(x):
    i=0
    while i<x:
        yield i**2
        i=i+1
b=int(input())
for i in sqr(b):
    print(i)
