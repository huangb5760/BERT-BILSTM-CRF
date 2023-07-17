import re

def replace(text,source_char,taget_char):
	pattern1 = re.compile(r'\d *'+source_char+' *\d')
	pattern2 = re.compile(r' *'+source_char+' *')
	search = pattern1.findall(text)
	print(pattern1)
	if search:
		print("search --> searchObj.group() : ", search)
		for item in search:
			print(item)
			fiter = pattern2.sub(taget_char,item)
			print(fiter)
			text = re.sub(item,fiter,text)
	return text

text='4.0+5.0*1500 0.75*1250    1.0  1.2  1.5 *1250 有花镀锌    麻烦你报个价'
text = re.sub(r'\n','<br />',text)
text = re.sub(r'[×xX]','*',text)
text = re.sub(r' *\* *','*',text)
text = re.sub(r' *(都是|/\*) *','*',text)
text = re.sub(r' *(或|？|\?|、|,|\+) *','/',text)
#今天普热卷4.0和5.0*1500包什么价？
text1='4.0+5.0*1500'
print(replace(text1,'(或|？|\?|、|,|\+)','/'))