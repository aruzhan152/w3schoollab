import re 
text = "Gh hgYUGyujhG jhygHJ" 
tx = re.sub(r'(\w)([A-Z])', r'\1 \2',text) 
print(tx)