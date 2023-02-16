nums=[int(a) for a in input().split()]
def Unique(nums):
    uniq=[]
    for a in nums:
        if a not in uniq:
            uniq.append(a)
    print(uniq)
    
cn=Unique(nums) 