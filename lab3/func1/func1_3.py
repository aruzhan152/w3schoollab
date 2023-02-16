def Solve(heads=35,legs=94):
    for R in range(heads):
        Ch=35-R
        if ((Ch*2)+(R*4))==legs:
            return f'Number of chiken = {Ch}\nNumber of rabbits = {R}'
       
cn=Solve()
print(cn)
        