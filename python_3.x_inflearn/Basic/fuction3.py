''' 사용자 정의 함수 
  
  def 함수명(인수):  
	  <실행할 명령1>
	  <실행할 명령2>
	  ...

  인수(매개변수, 파라미터)

'''
def show_max(a, b):
	if a > b:
		print (a, "는 최대값 이다")
	elif a == b:
		print (a, "와", b, "는 같다")
	else:
		print (b, "는 최대값 이다.")


show_max(10, 6)

i=5
j=5

show_max(i,j)

i=10
j=100

show_max(i,j)

def sum(a, b):
	return a+b

a = 40
b = 30

d = sum(a,b)
print(d)

def sum(a,b,c):
	return a+b+c

c = sum(10, 20, 30)

print(c)	
# sum 함수는 두개의 인자(a,b)를 통해서 입력을 받는다. 서로 더한 값을 돌려주는 함수이다.
# 돌려주는 값(리턴 값)을 받기 위해서는 받을 변수 필요하다.
# 리턴값을 받을 변수 = 함수명(인수1, 인수2, ...)

''' 일반적인 함수의 구조
   def 함수명(인수,...) :
	<실행할 명령>
	.....
	return 값

   [[ 인수가 없는 함수(입력값이 없는 함수) ]]
'''
def show():
	return "Hello"


aa = show()
print(aa)

# 인수도 없고 리턴값도 없는 함수

def show():
	print("안녕하세요")

show()

''' [[ 예상할 수 없는 인수를 갖는 함수 ]]
  
  def 함수명(*인수)
'''

def sum(*a):
	tot = 0
	for i in a:
		tot +=i # tot = tot+i
	return tot


res = sum(10, 20 ,30)

print(res)


res = sum(1,2,3,4,5,6)
print(res)

def cal(aa, *a):
	if aa == "sum":
		tot = 0
		for i in a:
			tot +=i
	elif aa =="mul":
		tot = 1
		for i in a:
			tot *=i
	return tot

res = cal("mul", 1,2,1,12)

print(res)

res = cal("sum", 1,2,1,11)

print(res)

# 리턴값의 유형

def return_value(a,b):
	return a+b

a = return_value(1,2)

print(a)

# return만 단독으로 사용할 경우에는 함수를 바로 빠져 나간다.

def show(aa):
	if aa == 0:
		return
	print("0이 아니다")

show(1)


# 인수에 초기값을 설정하기: 초기화 하고자 하는 인수는 마지막에 설정하자!!
def show(name, age, gender="M"):
	print("이름은 ", name)
	print("나이는 ", age)

	if gender == "M":
		print("남자")
	else:
		print("여자")

show("홍길동", 23)

show("김길녀", 21, "F")

def show(name, gender="M", age):
	print("이름은 ", name)
	print("나이는 ", age)

	if gender == "M":
		print("남자")
	else:
		print("여자")


show("홍길동", "F", 23)





  









