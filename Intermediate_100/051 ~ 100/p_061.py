import re

input_data = 'aaabbccccccasss'
rule = re.compile('[a-c]+')

one = re.findall('b', input_data)
two = re.findall(rule, input_data)
three = re.findall('(\\w)(\\1*)', input_data)

s = ''
for i, j in three:
    s += str(len(j)+1)+i
print(s)