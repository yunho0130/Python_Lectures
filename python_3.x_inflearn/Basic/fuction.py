''' 함수(function) : 재사용 가능한 프로그램, 명령 덩어리

   우리가 접했던 함수 중에 range(1,5) 함수는 이미 만들어져 있는(내장되어 있는)
   내장 함수였다. 앞에서 우리는 range()함수를 호출해서 사용했다

   함수는 프로그램을 작성할 때 필요한 중요한 단위이다.

   함수에는 내장함수, 사용자 정의 함수가 있다.

   함수를 사용하는 이유는 사용하기 편하게 하기 위해서....

   
   [[ 문자열 함수 ]]
     . 문자열 포맷팅 함수 format()
'''
#{n}는 자리표시자를 의미한다. 여기서 n은 format()에 지정된 위치(인덱스)를 표시한다.
print("you've {0} a friend".format("got"))

str = "{2} {0} {1}".format("a", 100, 200)

print(str)

number = 100
day = "sunday"

print("오늘은 우리가 사귄지 {0}일 째 되는 날!! 요일은 {1} !!".format(number, day))

#인덱스와 이름을 혼용해서 사용하기
print("오늘은 우리가 사귄지 {0}일 째 되는날 !! 요일은 {day}".format(300, day="sunday"))

#좌측 정렬
name="김말똥"
print("{0:<10}".format(name))
#우측정렬
print("{0:>10}".format(name))
#가운데 정렬
print("{0:^10}".format(name))

print("{0:-^20}".format(name))

#소문자를 대문자로 바꾸는 함수
aa = "hello"
aa1 = aa.upper()
print(aa1)
# 대문자를 소문자로 바꾸는 함수
aa2 = aa1.lower()
print(aa2)

#문자 갯수를 리턴하는 함수
aa = "abdcde"
cnt = aa.count('d')
print(cnt)

#문자열의 길이 구하는 함수
cnt = len(aa) #len(문자열)
print(cnt)

#문자 위치 찾기 함수:문자열에서 찾고자하는 문자의 첫번째 위치를 리턴하는 함수

bb = "cafdegfff"
loc = bb.find("h") # 찾고자 하는 문자가 없는 경우에는 -1을 반환한다.
print(loc)

'''
loc = bb.index("h")  #index함수는 find함수와는 다르게 찾고자 하는 문자가 없을 경우 에러가 난다.
print(loc)
'''
#공백지우기 함수(lstrip, strip, rstrip)
aa = "   good   "
print(aa.lstrip() +"morning")

print(aa.rstrip()+"morning")

print(aa.strip()+"morning")

#문자열 대체 함수(replace) : 문자열 내의 특정한 값을 다른 값으로 교체한다.
aa = "good morning Jane!!!"
bb = aa.replace("morning", "night") #바뀔 대상(문자열), 교체할 문자열 

print(bb)

#문자열 나누기(split)

str = "good morning jane!!!"
str_split = str.split() #split()괄호안에 값이 없으면 공백을 기준으로 문자열을 나눈다.

print(str_split)

str = "김말똥/28/서울시 강남구/010-1231-1235"
print(str.split('/'))#'/'를 구분자로 해서 문자열을 나눈다. 그 결과는 리스트에 저장된다.











