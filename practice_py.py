#문제1
# 1부터 100까지 숫자중에 3의 배수만 모두 더한 값을 출력

#for i range(int(100)):
 #   if i*3<100:
  #      print(i)

#문제2
# 'hello world python' 에서 각 단어의 첫 글자만 대문자로 바꿔줘

#문제3
#[3,1,4,1,5,9,2,6,5]에서 중복을 제거하고 큰 수 부터 정렬해 출력하는 함수 clean_sort(numbers)을 작성

#numbers= [3,1,4,1,5,9,2,6,5]
#print(numbers.sort)
'''
#day1_20260713
#1부터 50까지의 숫자 중에서 4의 배수가 아닌 수만 모두 더한 값을 출력하세요.
n =0
for i in range(1,51):
    if not i%4==0:
        n = n + i
print(n)

# day2_20260714
# 1부터 100까지의 숫자 중 7의 배수의 개수와 합을 각각 출력하세요.
print("=" *10, 'day2', "="*10)
n=0
k=0
for i in range(1,101):
    if i%7 ==0:
        n= n+1
        k = n*7 + k
        
print(n, "7의 배수 갯수")
print(k, "7의 배수의 합")      

# day3_20260715
# 나머지연산(%)과 조건문
# 1부터 50까지의 정수를 하나씩 확인하면서 3의 배수이면 그 수를 리스트에 담고, 마지막에 리스트와 그 개수를 출력하는 코드를 작성하세요.
# 기대 출력
# [3, 6, 9, ..., 48]
# 16
print('='*10, '3day', '='*10)
n=0
N=[]
for i in range(1,51):
    if i%3 == 0:
        n= n+1
        N.append(i)
print(N)
print(n, '3의배수의 갯수')

# day4_20260716
# 문자열 split/join
# 공백으로 구분된 단어들의 담긴 문자열이 있다.
# 이 문자열을 단어 단위로 나눈 뒤, 각 단어를 모두 대문자로 바꾸고, 하이픈으로 이어 붙여 출력하라.
# 입력 예시 
s= "reactor pump valve sensor"
# 기대 출력 REACTOR-PUMP-VALVE-SENSOR
A=s.upper().split(' ')
print(A)
#print(A)-> ['REACTOR', 'PUMP', 'VALVE', 'SENSOR']
result = '-'.join(A)
print(result)

# Day 5
data = ' reactor,pump,valve,heat exchanger '
#1. 양끝에 공백을 제거하라
#2. 쉼표로 분리해 리스트로 만들어라
#3. 각 이름을 대문자로 바꾼뒤 "|"로 이어 붙여라
# 기대출력
# ['reactor', 'pump', 'valve', 'heat exchanger']
# REACTOR | PUMP | VALVE | HEAT EXCHANGER
print('='*10, 'day5', '='*10)
DATA=data.strip().split(',')
print(DATA)
DATA=data.upper().strip().split(',')
print(DATA)
DATA_1 =' | '.join(DATA)
print(DATA_1)


#Day6

temp = [23, 25, 28, 31, 29, 26, 24]
# 1. 첫번째값과 마지막 값을 출력하하 (마지막값은 음수 인덱스 사용)
# 2. 가운데 3개값(28,31,29)을 슬라이싱으로 잘라 출력하라
# 3. 리스트를 역순으로 뒤집어 출력해라(슬라이싱만 사용, reverse()금)

# 기대출력
# 23 24
# [28,31,29]
# [24,26,29,31,28,25,23]

print('='*10, 'day6', '='*10)
print(temp[0], temp[-1])
print(temp[2:-2])
print(temp[::-1])

#Day7

text = "chemical"

#기대출력
#{'c':2, 'h':1, 'e':1, 'm':1, 'i':1, 'c':2, 'a':1, 'l':1}
#for과 딕셔너리 사용
t= {}
for i in text:
    if i in t:
       t[i]=t[i]+1
    else:
        t[i]=1
        
print(t)
'''
 






