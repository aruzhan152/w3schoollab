
path = r"C:\Users\anara\git_tutorial\work\w3schoollab\hub.py"

count = 0

with open(path, 'r') as file:

    for line in file:

        count += 1

print(count)