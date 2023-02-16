class Prime():
    
    def prime(self,nums):
        for num in nums:
            bool=True
            for x in range(2,num-1):
                if num%x==0:
                    bool=False
                    break
            if bool==True:
                p.append(num)
                

nums=[int(a) for a in input().split()]
    
p=[]        
cl=Prime()
cl.prime(nums)
print(p)   