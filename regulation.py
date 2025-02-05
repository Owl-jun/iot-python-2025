import re

text = " 37 rip vip voice 3 is voshg 9 2 opqrstu"
n_p = re.compile(r'\d+')

cleanText = re.sub(r'\s+','',text)

nums = re.findall(n_p,cleanText)
print(nums)



