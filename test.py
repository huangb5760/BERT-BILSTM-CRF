import re

text='0.9'
text = re.sub(r'\n','<br />',text)
text = re.sub(r'[xX]','*',text)
text = re.sub(r' +',' ',text)
text = re.sub(r' *\* *','*',text)
text = re.sub(r' *(都是|/\*) *','*',text)
text = re.sub(r' *或 *|？|\?|/+','/',text)
print(text)