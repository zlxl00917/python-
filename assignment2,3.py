'''
실습 2번
홀수단(1,3,5,7,9단) 출력하는 함수 gugudan_odd 함수 정의
짝수단(2,4,6,8단) 출력하는 함수 gugudan_even 함수 정의
인자가 홀수면 gugudan_odd 함수를 실행, 
짝수면 gugudan_even 함수를 실행하는 함수 gugudan_odd_or_even 함수 정의 및 실행
'''
print("실습 2번")
def gugudan_odd():
    i=1
    while i<10:
        for j in range(1,10):
            i+=2
            print("%d*%d"%(i,j))
                                                   
def gugudan_even():
    i=2
    while i<10:
        for j in range(1,10):
            i+=2
            print("%d*%d"%(i,j))
def gugudan_odd_or_even(num):
    if num%2==0:
        gugudan_even()
    else:
        gugudan_odd()

'''
실습 3번
주어진 숫자에 따라 구구단 출력하는 함수 정의 및 실행
인자로 숫자 하나를 받는다
해당 숫자만큼 구구단 출력
Ex) 인자가 5
1~5 단까지 출력
Ex) 인자가 8
1~8 단까지 출력
'''
print("실습 3번")
def gugudan(num):
    i=1
    while i<num:
        i+=1
        for j in range(1,10):
            print("%d*%d"%(i,j))

