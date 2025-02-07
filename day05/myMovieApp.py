# myMovieApp.py
from Movie import Movie as m
import re
import os

VERSION = 0.5

def clearScreen():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# 메인에서 제일처음 실행되는 함수
def run():
    clearScreen()
    movieList = []

    load_movie(movieList)
        
    while True :
        menu = set_menu()
        if menu == 1:                                               # 영화 입력
            movie = set_movie()
            movieList.append(movie)
            print(f"영화 입력이 완료 되었습니다. \n\n{movie}\n")
        elif menu == 2: get_movie(movieList)                        # 영화 출력
        elif menu == 3: search_movie(movieList)                     # 영화 검색
        elif menu == 4: del_movie(movieList)                        # 영화 삭제
        elif menu == 5:                                             # 앱 종료
            print("데이터 저장 후 앱을 종료합니다.")
            save_movie(movieList)
            break
        else : print("숫자만 입력하세요. [1-5] ")
        input("아무 key나 입력")
        clearScreen()

# 저장된 파일 로드
def load_movie(items : list):
    with open('.MyMovieList.txt', mode='r' , encoding='utf-8') as r:
        while True:
            temp = r.readline().replace('\n','')
            if not temp: break
            lines = temp.split('|')
            title, year, com, rate = [i for i in lines]
            items.append(m(title,year,com,rate))

## 프로그램 종료 시 저장된 데이터를 텍스트 파일에 저장
def save_movie(items : list):
    with open('.MyMovieList.txt',mode='w',encoding='utf-8') as f:
        for movie in items:
            f.write(f'{movie.get_title()}|{movie.get_releaseYear()}|{movie.get_company()}|{movie.get_rate()}\n')

## 영화 번호를 통한 삭제
def del_movie(items : list):
    d_idx = int(input("삭제할 영화 번호를 입력하세요. : "))-1       # 표기되는 번호가 실제 인덱스+1 이기 때문에, -1을 해준다.
    if d_idx in range(len(items)):                                  # 범위 초과 방지
        print(f'삭제가 완료되었습니다. {items[d_idx].get_title()}') 
        del(items[d_idx])
    else: print("삭제 할 수 없거나 , 번호가 존재하지 않습니다.")

## 영화이름 search 버전1 , re모듈 활용
def search_movie(items : list):
    s_name = input("검색어를 입력하세요 (제목) : ")
    p = re.compile(f'{s_name}+',re.I)
    try:
        idx = []
        for movie in items:
            if p.search(movie.get_title()): idx.append(items.index(movie)) # 이름이 포함되어 있다면 검색가능한 버전
        # idx = [index for index, value in enumerate(items) if value.get_title() == s_name] // 완전히 일치할 상황에만 검색가능한 버젼
        print()
        print('------------------------------')
        print(f'검색 값 \'{s_name}\' 으로 검색된 영화 입니다.')
        for i in idx: print(items[i])
        print('------------------------------')
        print()
    except Exception as e:
        print('해당 영화가 존재하지 않습니다.')

## 영화 이름 search 버전2 , 클래스 멤버함수 활용
def search_movie2(items : list):
    title = input('검색할 영화제목 입력 : ')
    for item in items:
        if item.isNameContain(title):
            print('------------------------------')        
            print(f'검색 값 \'{title}\' 으로 검색된 영화 입니다.')
            print(item)
            print('------------------------------')

## 영화 출력
def get_movie(items: list):
    print('현재 저장된 영화 리스트')
    for i in items:
        print('------------------------------')                
        print(f'{items.index(i)+1}.\n{i}')
        print('------------------------------')
        print()

## 영화 입력
def set_movie():
    while True:
        try:
            title, year, company, rate = input('영화입력[제목|개봉년도|배급사|평점] : ').split('|')
            year = int(year)
            rate = float(rate)
            break
        except Exception as e:
            print('잘못된 입력입니다. 입력예시 가나|2011|회사|3.5')

    movie = m(title,year,company,rate)
    return movie

## 메뉴 표시
def set_menu():
    str_menu = (f'------------------------------\n'
                f'내영화 앱 ver{VERSION}\n'
                f'1. 영화 입력\n'
                f'2. 영화 출력\n'
                f'3. 영화 검색\n'
                f'4. 영화 삭제\n'
                f'5. 앱 종료\n'
                f'------------------------------\n')
    print(str_menu)
    try:
        sel_menu = int(input('메뉴 번호입력 : '))
    except Exception as e:
        sel_menu = -1
    return sel_menu



## -------------------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------------------



if __name__ == "__main__" :
    print('내 영화 앱 시작')
    run()

print('프로그램 종료')


