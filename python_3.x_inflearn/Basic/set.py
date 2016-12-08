# -*- coding:euc-kr -*-

''' 집합 (Sets) :버전 2.3부터 지원되기 시작함
   
   집합에 관련된 것들을 쉽게 처리하기 위한 자료형 'set' 키워드를 이용하여 만들수 있다. '''

ss = set(['a', 'b', 'c'])

print(ss)

ss = set([1,2,3])
print(ss)

ss = set("Good Morning")
print(ss)

# 집합에 특징 :  - 중복을 허용하지 않는다.(중복을 제거하기위한 필터로 활용되기 한다.) - 순서가 없다.
# 리스트 튜플은 순서가 있다.따라서, 인덱싱을 이용하여 값을 얻어올 수 있다.
# 집합은 순서가 없기 때문에 인덱싱으로 값을 얻어올 수 없다. 딕셔너리 역시 순서가 없는 자료형이다.
# 집합과 딕셔너리는 인덱싱을 지원하지 않는다.
# 집합에 저장된 값을 인덱싱으로 접근하기 위해서는 리스트나 튜플로 변환 해야한다.

ss1 = set([1,2,3])
li = list(ss1)
print(li[2])

#교집합, 합집합, 차집합을 이용하자

s1 = set([1,2,3,4,5,6,7])
s2 = set([3,5,6,8,9])

#교집합은 '&' 기호를 이용하여 구한다.또는 intersection 함수를 이용한다.
print(s1 & s2)
print(s1.intersection(s2))

# 합집합은 '|' 기호를 이용한다. 또는 union 함수를 이용한다.
print(s1 | s2)

print(s1.union(s2))

# 차집합은 '-' 기호를 이용한다. 또는 difference 함수를 이용한다.
print(s1-s2)

print(s1.difference(s2))

#집합에 값을 추가하기 
s1 = set([1,2,3])
s1.add(100)#한개의 값을 추가 할때는 add를 이용한다.
print(s1)

s1 = set([1,2,3,4])
s1.update([10,100,1000])
print(s1)

#집합에서 값을 삭제하기
s1 = set([1,2,3,4,5])
s1.remove(5)
print(s1)

# 대칭 차집합 (^): 두개의 집합이 있을 때 둘 중 한집합에만 있는 항목들
s = set("Good Morning")
t = set("Good Night")

print(s ^ t)

s.remove('g')
#s.remove('h')

s.discard('h') #집합에서 항목을 제거한다. 집합내에 없는 항목을 제거 할때는 에러가 발생하지 않는다.
s.discard('G')

length = len(s)
print(length)

print(s)
#집합에서 모든  항목을 제거
s.clear()
print(s)





