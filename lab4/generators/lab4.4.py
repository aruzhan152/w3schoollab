def squares(x, y):
    i=1
    for i in range(x, y):
            yield i**2
            i=i+1


b=int(input())
k=int(input())
for i in squares(b, k):
    print(i)