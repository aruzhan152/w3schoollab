import re 
txt="hg_hjghj_______nbhjj" 
x=re.findall(r"([a-z]+)\_", txt) 
print(x)