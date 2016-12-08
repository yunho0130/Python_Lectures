''' [[ 파일 입출력 ]]
  
   . 파일 생성

   파일객체 = open(파일이름, 파일 열기모드)

   --- 파일 열기 모드 --
   .. r 모드 : 읽기모드 - 파일을 읽기 용도로 사용할때
   .. w 모드 : 쓰기모드 - 파일에 내용을 쓸 때 (쓰기모드로 열 때 
                                파일이 존재하는 경우에는 원래있던 내용이 모두 지워지고 열린다.
								파일이 존재하지 않을 경우에는 새로운 파일 생성된다.)
   .. a 모드 : 추가모드 - 파일에 새로운 내용을 추가 할 때

   '''
#fp = open("test_new.txt", 'w')

#close()는 생량해도 무방하다. 파이썬에서는 프로그램 종료시 열린 파일 객체들을 자동으로 닫아준다.
#그렇지만, 될수 있으면 직접 닫아주는것이 올바른 방법이다.
#쓰기 모드로 열었던 파일을 닫지 않고 재사용하는 경우에는 에러가 발생하기 때문에 
#닫아주는 습관을 갖자!!

#fp.close()


# 파일에 내용을 출력하기
fp = open("test_new.txt", 'w')

for i in range(1,5):
	content = "%d 번째 줄....\n" %i
	fp.write(content)

fp.close()

'''
for i in range(1,10):
	content = "%d 번째 줄...." %i
	print(content)
'''

''' -- 파일을 읽어오는 방법
   . 파일객체에서 사용할 수 있는 readline() 이용하기 '''

fp = open("test_new.txt", 'r')
data = fp.readline() # 읽어온 첫번째 라인을 리턴한다.
print(data)
fp.close()

fp = open("test_new.txt", 'r')

while True: #true, True는 서로 다르다. 참과 거짓을 나타내는 것은 True, False
	data = fp.readline() # 더이상 파일에서 읽어올 라인이 없는 경우에는 None을 리턴한다.
	if not data: break
	print(data)

'''
while 1:
	userData = input() # 사용자가 입력한(키보드로 입력한) 데이터를 콘솔에 출력하는 예
	if not userData: break
	print(userData)
  

   . readlines()를 이용하여 파일을 읽어오기
'''
fp = open("test_new.txt",'r')
datas = fp.readlines() #readlines() 리턴값이 리스트이다.
                               #이함수는 모든 라인을 읽어서 리스트에 리턴한다.

for data in datas:
	print(data) #data는 ['1 번째 줄....\n', '2 번째 줄....\n','3 번째 줄....\n','4 번째 줄....\n']

fp.close()

# . read() 함수를 이용한 파일 읽기
fp = open("test_new.txt", 'r')
data = fp.read() #read()함수는 파일 내용 전체를 문자열로 리턴을한다.
print("=========")
print(data)

fp.close()

# a 모드를 이용해서 파일에 내용을 추가하기
fp = open("test_new.txt", 'a')

for i in range(5,8):
	data = "%d번째 라인....\n" %i
	fp.write(data)
fp.close()

#with문을 이용해서 파일 객체 다루기 : with문을 이용하면 파일을 닫을 필요없다. 자동으로 파일을 닫아준다.

fp = open("test_2.txt", 'w')
fp.write("파일 입출력 테스트 2번째")
fp.close()

with open("test_2.txt", "w") as fp:
	fp.write("with문을 이용한 파일 입출력 테스트")



