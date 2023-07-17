import re

#替换数字中间的字符
def local_replace(text,source_char,taget_char):
	pattern1 = re.compile(r'\d *'+source_char+' *\d')
	pattern2 = re.compile(r' *'+source_char+' *')
	search = pattern1.findall(text)
	if search:
		for item in search:
			fiter = pattern2.sub(taget_char,item)
			text = text.replace(item,fiter)
	return text
#钢铁行业文本处理
def pre_handle_text_steel(text):
		text = re.sub(r'\n','<br />',text)
		text = local_replace(text,'[×xX]','*')
		text = local_replace(text,'\+','/')
		text = local_replace(text,'(都是|/\*)','*')
		text = local_replace(text,'(或者|或|和|？|\?|、|,)','/')
		return text