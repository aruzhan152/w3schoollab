import re 
def fun(text): 
    print(re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text).lower()) 
txt=str(input()) 
fun(txt)