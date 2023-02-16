def has_33(nums, cnt = 0): 
    for i in range(len(nums)- 1): 
        if nums[i] == nums[i+1]: 
            cnt += 1  
    if cnt > 0: 
        return True 
    else: 
        return False 
 
 
 
a = list(map(int, input().split())) 
print(has_33(a)) 


