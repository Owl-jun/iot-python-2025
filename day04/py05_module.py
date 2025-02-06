# py05_module.py

# 외부 모듈을 사용하기 위한 방법
# 내 컴퓨터에 없는 모듈을 가져와서 사용하려면
# pip : 파이썬이 제공하는 Package Installer of Python
# 터미널 > pip install requests
# https:// pypi.org 에서 설치할 패키지 검색

import requests

print('외부 패키지 사용')
# 웹 브라우저가 아닌 파이썬 상에서 웹사이트 접속
res = requests.get('https://www.google.com') # website URL

print(res.status_code) # 200 ( OK )
# print(res.content)

with open('./day04/index.html', mode = 'w', encoding = 'utf-8') as f :
    f.write(str(res.content, 'utf-8'))

class Sample:
    pass

sam = Sample()
print(sam)

## __main__ 프로그램이 시작하는 진입점(entry point)
## if __name__ == "__main__" :
## 이 구문은 이 파일을 직접실행 했을 때만 실행됩니다.

## C 언어 등의 static void main()와 동일한 역할
## __name__ 은 본인이 실행된 파일이라면 "__main__" 을 리턴
## import된 파일이라면 그 모듈의 이름을 리턴한다.