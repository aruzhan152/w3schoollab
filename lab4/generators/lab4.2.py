def even(x):
    i=0
    while i<x:
        if i%2==0:
            yield i
        i=i+1

b=int(input())

for i in even(b):
    print(i, end=', ')