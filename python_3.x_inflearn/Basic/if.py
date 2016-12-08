''' 제어문 (조건문, 반복문) : 프로그램의 흐름을  제어를 해서 효율적으로 이용하기 위한 명령문

  조건문 : if문
  반복문 : while, for문

  
  ** if 문 기본 구조 **

  if <조건문>:
	  <실행할 명령문 1>
	  <실행할 명령문 2>
	  .......
  else :
	  <실행할 명령문 1>
	  <실행할 명령문 2>
	  .......
 
 [indentation(들여쓰기)]
 if문을 작성할 때는 조건문 다음에 들여쓰기를 해줘야 한다.
 
 다른 언어에서는 
	 if <조건문>
	 {  <---- 파이썬에서는 들여쓰기로 대체
		<실행할 명령문1>
		<실행할 명령문2>
		<실행할 명령문3>
	 }else{
		<실행할 명령문1>
		<실행할 명령문2>
		<실행할 명령문3> 
	 }

  **
	 if <조건문> 다음에 반드시 ':' 와야 한다. ':' 다음에는 들여쓰기를 한다.
  
'''

number = 1; # 일반적으로 파이썬에서는 문장 끝에 ';' 생략하고 사용한다.

print (number);

if number:
	print("0이 아니다")
else:
	print("0이다")

''' 
** 비교 연산자

< : x < y --- x는 y보다 작다 
> : x> y --- x는  y보다 크다 
== : x==y --- x와 y는 같다 
!= : x!=y ---x와 y는 서로 다르다 
>= : x>=y ---x는 y보다 크거나 같다
<= : x<=y ---x는 y보다 작거나 같다

'''
x =100
y = 1000

print(x>y)

print(x!=y)

''' 논리 연산자 (and , or , not)

x and y : x와  y가 모두 참일 때 참
x or y : x와 y 둘중에 하나만 참일때 참
not x : x가 참이면 거짓

** in 연산자
x in 리스트, x not in 리스트, x in 튜플, x not in 튜플, x in 문자열, x not in 문자열

'''

print("a" in ["a", "b", "c"])

print("a" not in ["a", "b", "c"])

"a" in ("a", "b", "c")

print("a" in "abcd")


# 이중 if문
aa = ["a", "b"]
flag = 1

if 'c' in aa:
	print("a를 가지고 있습니다")
else:
	if flag:
		print("a를 가지고 있습니다")
	else:
		print("a를 가지고 있지 않습니다")

#elif (다른 언어에서의 else if 와 같다)

if 'c' in aa:
	print("c를 가지고 있습니다")
elif 'a' in aa:
	print("a는 가지고 있고, c는 가지고 있지 않습니다")
else:
	print("a와 c가 aa에 없습니다")

''' 다중 if문의 구조 (다른언어의 switch case문과 비슷한 구조)

if <조건문>:
	<실행할 명령문 1>
	<실행할 명령문 2>
	.....
elif <조건문>:
	<실행할 명령문 1>
	<실행할 명령문 2>
	....

elif <조건문>:
	<실행할 명령문 1>
	<실행할 명령문 2>
	....
...
else:
	<실행할 명령문 1>
	<실행할 명령문 2>
	...

** pass 

'''

dd = "d"

if dd in aa:
	pass
else:
	print(dd+"는 없습니다")


pp = ["a", "b", "c"]

# if문을 단일 문으로 처리하는 예
if dd in pp: pass
else: print("없습니다")
