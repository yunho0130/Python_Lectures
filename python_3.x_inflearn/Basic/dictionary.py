'''
>>> a = {1:"Hello!!"}
>>> a
{1: 'Hello!!'}
>>> a = {'first':['a','b','c']}
>>> a
{'first': ['a', 'b', 'c']}
>>> 
>>> sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
>>> 
>>> 
>>> sports["축구"]
'박지성'
>>> sports["야구"]
'강정호'
>>> 
>>> 
>>> aa = {1:"안녕"}
>>> aa[2] = "하이"
>>> aa
{1: '안녕', 2: '하이'}
>>> 
>>> 
>>> 


>>> 
>>> 


>>> aa[3] = "방가"
>>> aa
{1: '안녕', 2: '하이', 3: '방가'}
>>> aa["인사"] = "굿모닝"
>>> aa
{1: '안녕', 2: '하이', 3: '방가', '인사': '굿모닝'}
>>> aa[3] = [1,2,3]
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝'}
>>> aa[age] = 34
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    aa[age] = 34
NameError: name 'age' is not defined
>>> aa["age"] = 34
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝', 'age': 34}
>>> aa[0] = "adf"
>>> aa
{0: 'adf', 1: '안녕', 2: '하이', 3: [1, 2, 3], 'age': 34, '인사': '굿모닝'}
>>> 
>>> 
>>> 
>>> del aa[0]
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], 'age': 34, '인사': '굿모닝'}

딕셔너리 주의사항
-- key값(지수)은 고유한 값이므로 중복되는 값을 설정해 놓으면 안된다.
만약 중복이 된다면 하나만 적용되고 나머지는 제외된다.

키값으로 리스트는 쓸 수 없다. 튜플은 키 값으로 사용 가능하다.
키값은 값이 변할 수 없다는 전제하에 타입을 설정하면된다.

dict() 함수

'''

aa = dict() #항목(key:value)이 없는 딕셔너리를 만든다.
print(aa)

aa['one'] = "첫번째"
print (aa)


#keyList 만드는 함수(keys())
bb = {"name":"홍길동", "hp":"010-1234-1234", "age":24}
keyList = bb.keys() #리턴객체는 dict_keys
print(keyList)


for key in bb.keys(): #dict_keys 객체의 각 요소값을 출력
    print(key)

keyList1 = list(bb.keys())#dict_keys 객체를 리스트로 변환
print (keyList1)

#valueList 를 만드는 함수 (values())
valueList = bb.values()#리턴값은 dict_values객체이다.
print (valueList)

#key와 value 한쌍(항목)을 얻기(items())

item = bb.items()#리턴값은 dict_items객체이다. 이객체의 요소는 튜플로 구성된다.
                 #dict_items객체 : [('name', '홍길동'), ('hp', '010-1234-1234'), ('age', 24)] 
print(item)

#key:value 쌍을 모두 삭제하기(clear())
#bb.clear()
#print(bb)

#key값을 이용하여 value를 얻어오기(get)
age = bb.get('age')
print(age)

age = bb['age']#get함수를 이용하지 않고 사용하는 방법
print(age)

'''
gender = bb['gender'] 이때 키값이 존재하지 않으면 에러가 난다.
print(gender) '''

#get()함수는 키값이 존재하지 않을 경우에는 None값을 리턴한다.
gender = bb.get('gender')
print(gender)
print("=======get함수 실행후 bb 딕셔너리 ======")
print(bb)

#딕셔너리내에 키값이 없을 경우 디폴트값을 주는 방법
gender = bb.get('gender', '디폴트값')
print(gender)

#딕셔너리내에 해당 키가 존재하는지 알아보기
confirm_bb = 'gender' in bb
print(confirm_bb)

confirm_bb = 'name' in bb
print(confirm_bb)

#pop()함수를 이용해서 value값을 가져오기: 딕셔너리에 항목을 제거한다.
m = bb.pop('name')
print(m)
print("=========pop함수 실행후 bb 딕셔너리 ========")
print(bb)

bb["name"] = "홍길동"
print(bb)

m = bb.pop('gender','없음') #키가 없는 경우에는 디폴트값으로 대체 :pop(키 [,디폴트값])
print(m)

length = len(bb) #딕셔너리의 항목 갯수를 구함
print(length)







