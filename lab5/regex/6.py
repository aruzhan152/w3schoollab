import re 
 
txt="sdjf. .rgrergre.s, jkdgsu h" 
x = re.sub(r"[ \,\.]", ":", txt) 
print(x)