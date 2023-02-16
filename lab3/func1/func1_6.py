sent=[str(a) for a in input().split()]
def Reverse(sent):
    i=len(sent)-1
    while i>=0:
        print(sent[i], end = ' ')
        i-=1
    
cn=Reverse(sent)