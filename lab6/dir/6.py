#6
import os

path = r"C:\Users\anara\git_tutorial\work\w3schoollab\f"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in upper:

    os.chdir(path)

    open(letter + ".txt", 'a').close()