import os

p=os.listdir(r"C:\Users\anara\git_tutorial\work\w3schoollab")




print('Exists:', os.access(__file__, os.F_OK))

print('Readable:', os.access(__file__, os.R_OK))

print('Writable:', os.access(__file__, os.W_OK))

print('Executable:', os.access(__file__, os.X_OK))
