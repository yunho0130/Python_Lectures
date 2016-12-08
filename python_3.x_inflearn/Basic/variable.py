''' 변수(Variable)
:변수는 객체를 가리키고 있는 것이다. 참조변수라고 한다.

aa = 100

bb = 100

is (파이썬의 내장함수)를 이용해서 두개의 변수가
서로 같은 값을 갖고 있는 지 파악해 보자

aa is bb
'''
aa = 100
bb = 100
cc = 100

print(aa is bb)

#변수 삭제하기
del(aa)

#변수 선언 및 초기화
cc = dd = 100 # 여러개의 변수에 동일 값을 대입한다.

cc, dd = "국제시장", "명량"

print(cc)
print(dd)

(cc, dd) = ("aa", "bb")
print(cc)

[cc, dd] = ["하이", "파이썬!!"]

print(cc)
print(dd)

#데이터의 복사하는데 있어서 혼동하기 쉬운 예 
aa = ["a", "b", "c"]
bb = aa
aa[2] = "d"

print(aa)
print(bb)

#리스트의 복사
aa = ["a", "b", "c"]
bb = aa[:] #aa의 리스트를 처음 부터 끝까지 슬라이싱
aa[2] = "d"
print(aa)
print(bb)

''' 식별자 만들기 
  . 식별자의 첫문자는 알파벳 문자, 밑줄(_) 와야 한다.
  . 첫문자 이외의 나머지 글자는 밑줄, 숫자(0~9)가 올 수 있다.
  . 식별자는 대/ 소문자를 구분한다.
   예> myname과 myName 은 서로 다르다
  . 식별자는 공백이 들어가면 안된다.

  예> i, aa, name_1_2 (올바른 식별자)  2name,  a a b b, my-name, ?abc(잘못된 식별자)
'''











