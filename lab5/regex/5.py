import re 
 
txt="askdjhh ahjafb habd jhsdfjh ajjhbfabg" 

x=re.findall(r"\ba\w*b\b", txt) 
 
print(x)