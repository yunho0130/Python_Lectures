''' 리스트 함수들 : 문자열과 같이 리스트변수명 뒤에 .함수명 연결하여 사용한다.

 [ 리스트에 값을 추가하는 함수 ]
 '''
li = [10, 100, 1000]
li.append(11)
print(li)

li.append("ab")
print(li)

li.append(['a','b'])
print(li)

# [리스트 정렬함수]
li = [1,5, 10, 2,7]
li.sort()
print(li)

li = ['b', 'a', 'f', 'c']
li.sort() #기본적으로 오름차순 정렬을 한다.
print(li)

# [리스트 뒤집기 함수]
li.reverse() #sort()함수를 적용후 reverse()를 사용하면 내림차순 정렬이 된다.
print(li)

li = ['b', 'a', 'f', 'c']
li.reverse()
print(li)

# [요소의 위치를 반환하는 함수]
li = ['b', 'a', 'f', 'c']
aa = li.index('a')
print(aa)

'''
aa = li.index(1)
print(aa)
'''
# [ 요소를 삽입하는 함수]
aa = [1,2,3,4]
aa.insert(2, 5) # append함수는 무조건 제일 뒤에 추가시키지만, insert 함수는 원하는 위치에 추가 시킬수 있다.
print(aa)


# [요소를 제거하는 함수]
cc = [23,12,3, 6,5,3]
cc.remove(3) # 지우고자 하는 값이 여러개일 경우에는 첫번째 값을 제거한다.
cc.remove(3)
print(cc)

#[요소를 끄집에 내는 함수]
dd = [23,12,3, 6,5,3]
aa = dd.pop() #()안에 값이 없을 경우에는 리스트상의 마지막 값을 꺼내온다.
print(dd)
print(aa)

bb = dd.pop(1) #pop() 리스트의 요소(값)를 끄집어 내고, 끄집어낸 요소는 리스트에서 삭제를 한다.
print(bb)

#[요소의 갯수를 파악하는 함수]
dd = [23,12,3, 6,5,3]
cnt = dd.count(3) #count(요소) 요소의 갯수를 구하는 함수
print(cnt)

# [ 리스트 확장함수]
a = [1,2,3]
# a.extend([2,3,4,5])
print(a)

a += [2,3,4,5] #a = a+[2,3,4,5], *=(a*=1 --> a=a*1), -=(b-=1---> b=b-1)
print(a)






