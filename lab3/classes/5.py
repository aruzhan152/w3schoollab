class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f'Account owner {self.owner}/nAccount balance  {self.balance}'
    def Deposit(self,dep_b):
        self.balance+=dep_b
        print("balance topped up")
    def Withdraw(self,wd_b):
        if self.balance>=wd_b:
            self.balance-=wd_b
            print('withdraw accepted')
        else:
            print('withdraw not accepted')

  

a=int(input())
b=int(input()) 
c=str(input())          
cl=Account(c)
cl.Deposit(a)
cl.Withdraw(b)
print(cl.balance)
print(cl.owner)