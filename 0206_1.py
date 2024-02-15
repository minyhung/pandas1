import numpy as np #numpy 모듈을 가져와서 np라는 이름으로 가져와서 사용

ar = np.array([1,2,3]) # list를 이용해서 ndarray를 생성

#ndim은 몇 차원인지 확인
print(ar.ndim)

#shape 각 차원의 데이터 개수를 튜플로 리턴
print(ar.shape)

table=np.array([[1,2,3],[4,5,6]])

print(table.ndim)

print(table.shape)

print(table.dtype)

image = np.array([[[1,2,3],[1,2,3]],[[4,5,6],[7,8,9]]])
print(image.ndim)
print(image.shape)

ar=np.arange(1,10,2)
print(ar)

ar=np.empty(10)
print(ar)


#주대각선 방향이 1인 3*3 정방행렬 생성
ar=np.eye(3)
print(ar)

#행렬에서 주 대각선의 데이터만 골라서 배열을 생성
print(np.diag(ar))

#데이터 타입확인과 형 변환
ar = np.array([1,"2",3]) #숫자와 문자열을 가지고 배열을 생성 -문자
print(ar.dtype)

br = np.array([1,2.3,3]) #정수와 실수 혼합
print(br.dtype)

#ar 배열의 자료형을 정수로 변환
cr=ar.astype(np.int32)
print(cr.dtype)

#0부터 19까지 숫자를 가지고 1차원 배열 생성
ar=np.arange(20)
print(ar)

#ar을 4*5짜리 2차원 배열로 변환
#5대신에 -1을 대입해도 결과는 동일합니다.
#20개의 데이터는 4행으로 만들려면 5열 밖에 안됩니다. 
matrix= ar.reshape((4,5))
print(matrix)

#다차원 데이터를 1차원으로 변환
br = matrix.reshape(-1)
br=matrix.flatten()
print(br)

#배열에서 하나의 요소 접근
ar=np.arange(10)
matrix=ar.reshape((2,-1))
print(ar[0])  #첫번째 데이터
print(ar[-1])  #마지막 데이터
print(matrix)

#이차원 배열에서 요소 접근
print(matrix[0,2])
print(matrix[0][2])

#배열에서 범위를 이용한 접근

ar=np.arange(10)
matrix=ar.reshape((2,-1))

#일차원 배열에서 접근
'''
print(ar[1:4])  #1,2,3
print(ar[5:])   #5,6,7,8,9
print(ar[:4])   #0,1,2,3
print(ar[:])    #0~9
'''

#이차원 배열에서의 접근
print(matrix[1][1:3])  #6 7
print(matrix[1])  #1행전체
print(matrix[:,1])  #1열 전체

#배열생성
ar=np.arange(10)
print(ar)
#범위를 이용해서 데이터를 가져오는 것 - 참조를 복사합니다. 
br=ar[0:4].copy()

#데이터를 복제해서 br이 가리키도록 합니다. 
br=ar[0:4].copy()
print(br)

#br[0]을 수정하면 ar의 데이터도 영향을 받게 됩니다.

br[0]=42
print(br)
print(ar)

ar=np.arange(10)

#Fancy Indexing
br=ar[[1,3,5,7]]
print(br)
br[0]=15700
print(br)
print(ar)


matrix= ar.reshape((2,-1))

print(matrix)

print(matrix[:,0])
#이차원 배열에서 list를 이용해서 행 번호나 열 번호를 지정하면 이차원 배열이 만들어집니다.
print(matrix[:,[0]])
#numpy의 ndarray 나 pandas의 DataFrame에서
#하나의 열을 선택할 때 list로 설정하는 경우는 구조를 유지하기 위해서 입니다.

#이차원 배열
matrix = ar.reshape((2,-1))

#브로드캐스트 연산
#차원이 다른 경우 차원을 순회하면서 연산을 수행함.
print(matrix + 10)
data = np.array([100,200,300,400,500])
print(matrix+data)

print(matrix)
print(ar)
#브로드 캐스트 연산
#numpy의 ndarray와 논리연산을 수행하면 bool 배열이 만들어집니다.
print(ar==3)
#인덱스의 bool 배열을 대입하면 True 인 데이터만 추출됩니다.
print(ar[ar%2==1])

#홀수이거나 4의 배수인 데이터만 골라내기
print(ar[(ar&2==1) | (ar%4==0)]) # or 쓸때 왼쪽이 true일 확률이 높은거 둬야함.
# 영어 or을 그대로 쓰면 오류 출력

