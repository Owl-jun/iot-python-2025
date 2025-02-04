import re 

problem = "010-9501-1650"
p = re.compile("(\d{3})[-](\d{4})[-]\d{4}")
print(p.sub("\g<1>-\g<2>-****",problem))


