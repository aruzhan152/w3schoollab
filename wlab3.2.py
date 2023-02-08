#1
def conv(grams):
    return grams*28.3495231

#2
def convert(fah):
    return (5 / 9) * (fah - 32)

#3
def solve(numheads, numlegs):
    chick = numheads
    rab = 0
    while(numlegs > 0):
        if(numheads == rab+chick and rab*4+chick*2 == numlegs):
            print("There are", rab, "rabbits and", chick, "chickens")
            break
        else:
            rab += 1
            chick -= 1

#4
def filter_prime(listOfNum):
    ls = [int(x) for x in listOfNum.split()]
    return list(filter(lambda x: all(x%i != 0 for i in range(2,int(x**0.5)+1)) and x != 1, ls))

#5
from itertools import permutations

def findPer(string):
    words = [''.join(perm) for perm in permutations(string)]
    print(set(words))

#6
def rever(string):
    l = string.split()
    for i in range (len(l)):
        print(l[-(i+1)])

#7
import re
def det(l):
    string = ""
    for ch in l:
        string += str(ch)
    print(string)
    if "33" in string: return True
    else: return False

#8
def spy_game(nums):
    string = ""
    for ch in nums:
        if ch == 0 or ch == 7:
            string += str(ch)
    if "007" in string: return True
    else: return False

#9
def vol(rad):
    return 3.141*4/3*rad**3

#10
def uniqq(l):
    b = list()
    for i in range(len(l)):
        if l[i] not in b:
            b.append(l[i])
    return(b)

#11
def isPalindrome(string):
    for i in range(int(len(string)/2)):
        if(string[i] != string [-(i+1)]):
            return False
    return True

#12
def histogram(l):
    for x in l:
        print('*'*x)

#13
import random
def play():
    name = str(input("Hello! What is your name?\n"))

    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    count = 1
    randomm = random.randrange(1, 20)
    guess = int(input("Take a guess.\n"))
    while(guess != randomm):
        if(guess < randomm):
            print("Your guess is too low")
        if(guess > randomm):
            print("Your guess is too high")
        count += 1
        guess = int(input("Take a guess.\n"))
    print("Good job, " + name + "! You guessed my number in", count, "guesses!")

#14
from L1 import conv
from L2 import convert
from L3 import solve
from L4 import filter_prime
from L5 import findPer
from L6 import rever
from L7 import det
from L8 import spy_game
from L9 import vol
from L10 import uniqq
from L11 import isPalindrome
from L12 import histogram
from L13 import play

print(conv(13))
print(convert(100))
solve(35,94)
print(filter_prime("1 2 3 4 5 6 7 8 9"))
findPer("afg")
rever("We are ready")
print(det([1, 3, 1, 3, 3]))
print(spy_game([1,2,4,0,0,7,5]))
print(vol(3.3))
print(uniqq([1,1,2,3,3,4,7,5,4,2,1,7, "a", "b", "a"]))
print(isPalindrome("madam"))
histogram([2, 5, 3])
play()
