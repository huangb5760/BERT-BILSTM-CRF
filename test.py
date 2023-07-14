import re

pattern1 = re.compile(r' *\* *')
result1 = re.sub(r' *\* *','*','2.95/3.0 *950/1000   镀锌 ，看看')
print(result1)
result2 = re.sub(r' *(都是|/\*) *','*','2.95或 3.0 都是1000   镀锌 ，看看')
print(result2)
result3 = re.sub(r' *或 *|？|\?|/+','/','1.45？1250冷卷')
print(result3)