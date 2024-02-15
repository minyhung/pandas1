import numpy as np
import pandas as pandas

#연습
#데이터가 None이면 0, 
#100보다 크면 100으로 한 결과 배열 생성

#None과 같이 크기비교할 수 없는 데이터가 먼저 들어오면, 에러가 남
#그래서 none을 0으로 먼저 변환해준 후에 100보다 큰 수를 걸러내는 작업을 해야함
'''

ar = np.array([80, 70, 80, None, 120])

def processing(x) -> int:
	if x == None:
		return 0
	
	elif x>100:
		return 100
	
	else:
		return x

vectorized_func=np.vectorize(processing)
result=vectorized_func(ar)
print(result)


#행렬의 전치 - 축변경
original = np.array([[1,2,3],[4,5,6]])
print(original)
print(original.T)
print(original.transpose(1,0))

#랜덤한 숫자 추출의 개념
result=np.random.normal(size=5)
print(result)

#seed를 설정하지 않으면 실행시간을 기준으로 seed가 설정되므로
#실행할 때 마다 다른 숫자가 리턴


#seed를 42로 고정하면 실행할 때 마다 동일한 데이터가 리턴됩니다.
#머신러닝에서는 seed를 고정시키고 작업을 수행합니다. 
np.random.seed(seed=42)
result=np.random.normal(size=5)
print(result)

result=np.random.randint(low=1,high=45,size=6)
print(result)

#4행 3열짜리 배열 생성
matrix = np.arange(1,13).reshape((4,-1))
print(matrix)
#전체 데이터의 합계
print(np.sum(matrix))

#열의합계
print(np.sum(matrix, axis=0))
#행의합계

#피보나치 수열
#첫번째와 두번짼 무조건 1이고 세번째부터는 앞 2개의 항의 합으로 만들어지는 수열
#1,1,2,3,5,8,13,21,34,55 ...

def fibo(n:int) -> int:
	if n==1 or n==2:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)
	
print(fibo(10))

def norecursion_fibo(n:int)->int:
	n1=1
	n2=1
	v=1
	for i in range(3, n+1):
		v=n1+n2
		n2=n1
		n1=v
	return v
print(norecursion_fibo(100))

#표준편차와 분산은 ddof 옵션에 따라 값이 다르게 나옵니다.
#표준편차와 분산은 평균이라는 통계값을 가지고 구하게 되는데 
#평균이 결정되면 전체 데이터 개수 -1 만큼의 값을 알게 되면 
#나머지 1개의 값은 자동으로 결정됩니다.
#자동으로 결정되는 값을 빼고 계산하거나 포함시켜 계산할 수 있습니다.
#이 옵션이 ddof 옵션입니다.

print(np.var(matrix))
print(np.var(matrix, ddof=1))

print(np.cumsum(matrix))
print(np.cumsum(matrix, axis=1))


#배열 생성
ar=np.array([10,2,3,4,np.nan,32,42])

#배열에 None 데이터가 있는지 확인
print(np.isnan(ar)) #결측치 확인

#결측치를 제외하고 가져오기
temp = ar[np.logical_not(np.isnan(ar))]
print(temp)


#결측치를 제외하고 가져오기 - 결측치를 제거하지 않고 수행하면 nan이 포함됩니다.
#ar을 가지고 수행하면 np.nan이 포함되고 result를 가지고 수행하면 np.nan이 제거
result = ar[np.logical_not(ar > 10)]   # not 하면 True와 False가 바뀜
print(result)

'''
# 두 번째 부분
ar = np.array([2, 5, 23, 43, 21, 42, np.nan, 25])

# np.isnan() 함수를 사용하여 NaN 값을 제외하고 배열 생성
temp = ar[np.logical_not(np.isnan(ar))]

# 3의 배수이거나 4의 배수인 요소들 추출
result = temp[(temp % 3 == 0) | (temp % 4 == 0)]
print(result)

#아래 데이터는 1,2,3,4 중에 하나를 선택하는 범주형 데이터의 집합
#이상한 값이 있는지 확인

ar = np.array([2, 1, 3, 4, 5, 1, 2, 3])
print(np.unique(ar))

ar = np.array([2, 1, 3, 4, np.nan])
ar.sort()
print(ar)

#numpy의 sort는 리턴을 하고 ndarray의 sort는 리턴하지 않습니다.
#내림차순 정렬은 numpy의 sort를 이용하면 됩니다.
print(np.sort(ar)[::-1])

#2차원 배열은 numpy에서는 sort를 잘 사용하지 않습니다.
#데이터의 인덱스가 깨져버립니다. 

matrix=np.array([[1,3,2,4],[9,4,1,8]])
matrix.sort()
print(matrix)


#htstack
ar=np.array([[1,2,3],[4,5,6]])
print(ar)
br=np.array([[11,22,33],[44,55,66]])
print(br)

print(np.hstack([ar,br]))
print(np.vstack([ar,br]))
print(np.dstack([ar,br]))


np.save('ar.npy', ar)

import pandas as pd

#시리즈를 생성
price=pd.Series([1000,3000,2000,4000])
#시리즈를 출력 - 자동 생성된 인덱스와 값이 출력

print(price)
#1이라는 인덱스를 가진 데이터를 조회
print(price[1])
#인덱스를 직접 설정
price.index=['사탕','과자','음료수','탕후루']
print(price)
#인덱스가 사탕이라는 데이터를 조회 : 1000
print(price["탕후루"])

x=price["사탕":"음료수"]  #사탕부터 음료수까지의 데이터의 참조를 가져온 것
#x의 데이터를 변경하면 원본인 price의 데이터도 수정
x["사탕"]=800
print(x)
print(price)

print("=======================")

y=price[["사탕","음료수"]]   # 사탕과 음료수의 데이터를 복제해온 것
#y의 데이터를 변경해도 원본인 price의 데이터는 변경되지 않는 것
y["사탕"]=2000
print(y)
print(price)


s1=pd.Series([100,200,300,np.nan],index=["사과","배","한라봉","천혜향"])
#print(s1)
s2=pd.Series([100,200,300,500],index=["사과","한라봉","천혜향","무화과"])
print(s2)

#시리즈는 인덱스를 일치하는 데이터끼리 연산을 수행합니다.
#한쪽에만 존재하거나 np.nan인 데이터가 있으면 결과가 np.nan이 됩니다.

print(s1+s2)


#DataFrame 생성
source={
	'code':[1,2,3,4],
	'name':['카리나','지젤', np.nan,'윈터'],
	'age':[23,22,34,21]
}

df=pd.DataFrame(source)
print(df)

print(df.head(2))  # 앞에서 2개

print(df.tail(2))  

print(df.values)
print(type(df.values))

#print(dir(df))
help(df.isnull)


