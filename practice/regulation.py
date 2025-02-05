# 정규식 연습, 숙달

import re

text = " 37 rip vip voice 3 is voshg 9 2 opqrstu"
n_p = re.compile(r'\d+')

cleanText = re.sub(r'\s+','',text)

nums = re.findall(n_p,cleanText)
print(nums)




textList = ["1995-08-09", "1998-08-30", "2000-12-19", "1997-06-17"]

# 1998년 1월 1일 이후의 날짜를 찾기 위한 정규 표현식
pattern = r'^(199[8]|200[0-9]|20[1-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'

# 필터링
filtered_list = [date for date in textList if re.match(pattern, date)]
print(filtered_list)
