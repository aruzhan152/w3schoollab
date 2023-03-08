import os

p=os.listdir(r"C:\Users\anara\git_tutorial\work\w3schoollab")

for i in p:

    if os.path.isdir(i):

        print(i)

for i in p:

    if os.path.isdir(i) or os.path.isfile(i):

        print(i)

for i in p:

    if os.path.isfile(i):

        print(i)