def zero(x):
    i=x
    while i>=0 :
            yield i
            i=i-1

b=int(input())
for i in zero(b):
    print(i)
