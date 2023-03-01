import re 
 
txt="GHJHGy gGgyGUGhGYh Hu8UJHGHUYGGH YyuYUG" 
x=re.findall(r"[A-Z][a-z]", txt) 
print(x)