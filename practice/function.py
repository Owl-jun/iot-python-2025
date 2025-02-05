# *args 매개변수 , 가변 개수를 받을 수 있으며, 튜플로 들어온다.
def add(opt, *nums) :
    result = 0
    if opt == "add" :
        for i in nums :
            result += i
        return result
    
    if opt == "sub" :
        for i in nums :
            result -= i
        return result
print(add("add",3,4,5))

# **kwargs 매개변수 , 딕셔너리 형식의 인자가 들어온다.
def test(**kwargs) :
    print(kwargs.keys())
    print(kwargs.values())
test(name = "jun") ## 인자 전달 방법

# range 함수를 직접 만들어보기 !
def my_range(*args) :
    if len(args) == 1 :
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2 :
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 3 :
        start = args[0]
        stop = args[1]
        step = args[2]
    else :
        raise TypeError("my_range expected at most 3 arguments, got {}".format(len(args)))

    if step == 0:
        raise ValueError("step must not be zero")
    
    current = start
    if step > 0 :
        while current < stop :
            yield current
            current += step
    else :
        while current > stop :
            yield current
            current += step


for i in my_range(8) :
    print(i)

# lambda 연습

add = lambda x,y : x+y
result = add(3,4)

_addFunction = lambda *args : sum(args)

print(_addFunction(1,1,1,1,1,1,1))

my_lam = lambda **args : print(args.keys)
my_lam(name="ksj")