import os

p=(r"C:\Users\anara\git_tutorial\work\w3schoollab\delete.txt")

if os.path.exists(p):

    os.remove(p)

else:

    print("this file doesnt exist")

