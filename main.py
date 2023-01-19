# 9.3

def test(func):
    def hello_function(*args, **kwargs):
        print('start')
        # print('위치 기반 인수들:', args)
        # print('키워드 기반 인수들:', kwargs)
        result = func(*args, **kwargs)
        print('end')
        return result
    return hello_function

@test
def mission1():
    print("전나경의 과제입니다.")

mission1()