import re 
text = "HGvGgyBujGYjk" 
tx = re.sub(r"(\w)([A-Z])", r"\1 \2",text) 
print(tx)
