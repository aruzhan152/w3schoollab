nums=[int(a) for a in input('Enter all numbers by space! ').split()]
def Solve(nums):
    prime=[]
    for num in nums:
        bool=True
        for x in range(2,num-1):
            if num%x==0:
                bool=False
        if bool==True:
            prime.append(num)
    return prime
                
cn=Solve(nums)
print(f'Prime numbers are: {cn}')

  