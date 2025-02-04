# iot-python-2025
iot 개발자 기초 프로그래밍 언어 리포지토리

## 1일차
- 개발환경 설정
    - 압축, 폰트, 개발용 에디터 설치
        - 반디집 (교육, 회사에 전부 무료)
        - 나눔글꼴 중 D2Coding , 추후 나눔고딕코딩 필요
        - NotePad++ , git , github desktop
    - Visual Studio Code 설치
        - 확장 : Korean
        - 설정 : Font Family , mouse wheel zoom , Font Size

- 프로그래밍 언어 종류
    - 컴파일러(실행파일 생성) 
        - C, C++, C#, Java, ...
    - 인터프리터(소스코드를 바로 실행, 실행파일 없음)
        - 파이썬, JavaScript, Ruby, PHP ...
    
- 파이썬(Python)
    - 1990년에 개발한 인터프리터 언어
    - 네덜란드 개발자 귀도 반 로섬
    - 객체지향 프로그래밍 언어(Object Oriented Program)
    - 아주 쉽게 학습할 수 있는 언어

- 파이썬 개발환경 Pyenv
    - 파이썬 버전을 손쉽게 변경할 수 있는 툴
    - 파워쉘 관리자 모드, 아래 명령어 실행
        ```shell
        > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
        ```
    - https://github.com/pyenv-win/pyenv-win , 퀵 스타트 참조

- Visual Studio Code
    - Python 확장 설치
    - *.py 파일 생성 후 코딩
    - Ctrl+F5로 실행

## 2일차
- 파이썬 기초
    - 변수
        - `데이터`를 담아서 다른 곳에서 사용하기위해 사용
    - 자료형
        - None(null), int, float, bool, string, list, tuple, dict, set, ...
        - type() 함수로 <class 'str'> 확인가능
    - 화면입출력 : 콘솔에서 입력하고 결과 출력
        - input(), print()
    - 문자열 포맷팅 
        - 문자열을 좀 더 깔끔하게 표현
        - %s, %d, %f, %o, %h, %b ...
        - {0}, {1}, {2} ...
        - f"{}string"
    - 연산자
        - 기본연산 : + - * / // % ** ()
        - 리스트연산 : [] , [m:n]
        - 문자열메서드 : split('target') , replace('target','replace') , strip() , find() , upper() , lower() ...

- 깃허브
    1. **fetch origin** : 리모트-로컬 최신화
    2. pull : 리모트의 변경사항을 로컬로 다운로드
    3. commit : 로컬, 리모트에 변경사항을 저장
    4. push : 로컬의 변경사항을 리모트로 업로드
    


## 3일차
- 파이썬 기초
    - 흐름제어
        - if : 참을 기준으로 분기
        - for : 반복문 (보통 범위를 지정하여)
        - while : 반복문 (무한반복)
    - 파일 입출력
        - with open('경로',mode='r''w''a',encoding='utf-8') as 변수 :
        - 변수.write() , 변수.readline() ... , with as 문이라 자동으로 닫힘
    - 함수
        - y = f(x)
        - 자주 사용할 로직을 묶어놓은 덩어리
        - 함수 호출
        ```python
        def function(param):
            logic1
            logic2
            ...
            ...
        ```
    - 객체지향
        - 현실세계와 동일하게 프로그래밍 하겠다는 설계방식
        - 객체의 틀이 되는 클래스를 선언
        - 클래스 : 명사(멤버변수)와 동사(멤버함수==메서드)의 집합
        ```python
        class Object:
            # 멤버변수
            def 멤버함수(self,param):
                # logic ...
        ```

## 4일차
- 파이썬 기초
    - 객체지향 한번 더
    - 모듈, 패키지
    - 예외처리
    - 디버깅

## 궁금한 점들
- 이터레이터를 사용하는 이유
    - 리스트, 세트 등의 큰 용량의 객체를 통째로 스택에 가져오는것이아니라, 시작주소를 담은 이터레이터를 통해 메모리 효율을 증가시킨다.
    - for 문 등을 사용할때 코드의 간결성에 도움이 된다.
- 제네레이터 yield
    - yield 는 대용량의 데이터를 처리할 때 메모리 효율을 높혀준다.
    - 이터레이터와 비슷하지만 다르다. (값을 한번 받으면 다음 함수 실행을 기다린다.)
    - 궁금증 : 그렇다면 함수를 호출했을때, 스택 메모리영역에 올라와있을텐데, next() 메서드가 호출되지 않는다면 어떻게 되는거지?
        - A : 스택에서 해제됨, but 중단 된 상태를 힙 메모리에 있는 제너레이터 객체가 저장하고 있음.

## 정규식 학습
- 정규식
    - '[ ]' 문자 - 문자 클래스
        - 정규 표현식이 [abc]라면 이 표현식의 의미는 ‘a, b, c 중 한 개의 문자와 매치’를 뜻한다. 
        - 이해를 돕기 위해 문자열 "a", "before", "dude"가 정규식 [abc]와 어떻게 매치되는지 살펴보자.
            - "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치된다.
            - "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치된다.
            - "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않는다.
            - [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미한다. 예를 들어 [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일하다.

    ```
    자주 사용하는 문자 클래스
    [0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식이다. 이렇게 자주 사용하는 정규식은 별도의 표기법으로 표현할 수 있다. 다음을 기억해 두자.

    \d - 숫자와 매치된다. [0-9]와 동일한 표현식이다.
    \D - 숫자가 아닌 것과 매치된다. [^0-9]와 동일한 표현식이다.
    \s - 화이트스페이스(whitespace) 문자와 매치된다. [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈칸은 공백 문자(space)를 의미한다.
    \S - 화이트스페이스 문자가 아닌 것과 매치된다. [^ \t\n\r\f\v]와 동일한 표현식이다.
    \w - 문자+숫자(alphanumeric)와 매치된다. [a-zA-Z0-9_]와 동일한 표현식이다.
    \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치된다. [^a-zA-Z0-9_]와 동일한 표현식이다.
    대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.
    ```

    - '*' 문자 : 0회 이상 반복? , 메타 문자의 반복 개수가 무한대라고 표현했는데, 메모리 용량에 한계가 있어 실제로는 약 2억 개라고 한다.
    - '+' 문자 : 1회 이상 반복?
    - .(dot) 문자 - \n을 제외한 모든 문자

    - {} 문자와 ? 문자
        - {m} : 반드시 m번 반복
        - {m,} : m회 이상 반복?
        - {,m} : m회 이하 반복?
        - {m,n} : m회 이상 n회 이하 반복?
        - ? : {0,1} 과 같다.
    
    - 파이썬에서 사용하기
        - import re
        - p = re.compile('[a-z]+')

        - match() , idx 0 부터 검색시작, 처음부터 똑같다면 match 객체를 리턴, 없다면 null
            - m = p.match("python"); n = p.match("3 python")
            - print(m); print(n);
            - 결과 : <re.Match object; span=(0, 6), match='python'> \n None

        - search() , 인덱스 상관없이 값이 있다면 객체를 리턴 , 없다면 null
            - m = p.search("python"); n = p.search("3 python")
            - print(m); print(n);
            - 결과 : <re.Match object; span=(0, 6), match='python'> \n <re.Match object; span=(2, 8), match='python'>

        - findall() , 매치되는 모든 값을 리스트로 반환한다.
            - result = p.findall("life is too short")
            - print(result)
            - ['life', 'is', 'too', 'short']

        - finditer() , 매치되는 모든 값을 반복자로 반환한다.
            - result = p.finditer("life is too short")
            - (사용예시) -> for r in result: print(r) 

        - Match 된 객체의 메서드
            - group() : 문자열 리턴
            - start() : 시작 위치 리턴
            - end() : 끝 위치 리턴 (마지막 인덱스 +1)
            - span() : 시작 ~ 끝 튜플 리턴

        - re 모듈의 편의기능
            - p = re.compile("[a-z]+")
            - m = p.match("python")
            - m = re.match("[a-z]+","python") <= 위 두 줄을 한 줄로 축약
            
    - 컴파일 옵션
        - DOTALL(S) : .(dot)이 줄바꿈 문자(\n)를 포함해 모든 문자와 매치될 수 있게 한다.
            - p = re.compile('a.b', re.DOTALL) || (re.S)

        - IGNORECASE(I) - 대소문자에 관계없이 매치될 수 있게 한다.
            - p = re.compile('[a-z]+', re.I)
        
        - MULTILINE(M) - 여러 줄과 매치될 수 있게 한다. ^, $ 메타 문자 사용과 관계 있는 옵션이다.
            ```
            # multiline.py
            import re
            p = re.compile("^python\s\w+")

            data = """python one
            life is too short
            python two
            you need python
            python three"""

            print(p.findall(data))
            ```
            --> ["python one"]

            각 줄마다 적용시키고 싶다면
            ```
            # multiline.py
            import re
            p = re.compile("^python\s\w+", re.MULTILINE)

            data = """python one
            life is too short
            python two
            you need python
            python three"""

            print(p.findall(data))

            ```
            --> ['python one', 'python two', 'python three']

        - VERBOSE(X) - verbose 모드를 사용할 수 있게 한다. 정규식을 보기 편하게 만들 수 있고 주석 등을 사용할 수 있게 된다.
            
            ```
            charref = re.compile(r"""
            &[#]                # Start of a numeric entity reference
            (
                0[0-7]+         # Octal form
            | [0-9]+          # Decimal form
            | x[0-9a-fA-F]+   # Hexadecimal form
            )
            ;                   # Trailing semicolon
            """, re.VERBOSE)

            ```
            - [] 안에 있는 화이트스페이스 제외한 모든 화이트스페이스 제거된다.

            - 역슬래시 : \\ == "\" 와 같다. "\\" 를 쓰려면  \\\\



