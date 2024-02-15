### 컬럼이나 인덱스 변경
#컬럼 이름 변경

import numpy as np
import pandas as pd
'''
#item.csv 파일의 데이터를 가져와서 Data Frame 만들기
item=pd.read_csv('./data/item.csv')
#print(item)

names={"code":"코드","manufacture":"원산지","name":"이름","price":"가격"}
#numpy나 pandas의 대다수의 메서드는 원본을 변경하지 않고 수정해서 리턴
#pandas의 DataFrame에서는 inplace 옵션이 있는 경우 이 옵션에 True를 설정하면
#원본을 수정

item.rename(columns=names, inplace=True)

#print(item)

###인덱스 설정
#이 경우는 item에서 코드를 가져와서 인덱스로 설정 -But 코드는 컬럼으로 여전히 존재
#item.index=item.코드
#print(item)
#set_index를 이용하면 컬럼에서 제거되고 인덱스로 설정
#print(item.set_index("코드",inplace=True))   #이 코드는 한번만 수행해야 함

#인덱스를 다시 컬럼으로 만들고 0부터 시작하는 일련번호로 인덱스를 생성
item.reset_index(inplace=True)
print(item)


##데이터 삭제
#행이나 열 살제

#item.csv 파일의 데이터를 가져와서 Data Frame 만들기
item=pd.read_csv('./data/item.csv')
print(item)

#2행 삭제
print(item.drop([1],axis=0))
#code열 삭제
print(item.drop(['code'],axis=1))
'''

###데이터 추가 및 삭제
item=pd.read_csv('./data/item.csv')
# item.info()

#컬럼추가
item['description']= '과일'
# print(item)

#컬럼수정 => list는 순서대로 대입
item['description']=['사과','수박','딸기','바나나','망고','체리']
#print(item)

#컬럼수정 - Series나 dict는 인덱스나 키 이름대로 대입
item['description']={0:'사과',1:'수박',2:'딸기',4:'바나나',6:'망고',3:'체리'}
#print(item)

#행추가 
item.loc[6]=[7,'제주도','orange',3000,'한라봉']
# print(item)

#특정 셀 수정 => 앞에 인덱스를 설정하고 뒤에는 컬럼이름을 설정함.
item.loc[6,'name']="fig"
# print(item)

##DataFrame 연산
item1={
	"1":{'price':1000},
	"2":{'price':2000}
}

item2={
	"1": {"price":1000},
	"3":{"price":3000}
	
}

df1=pd.DataFrame(item1).T
#print(df1)

df2=pd.DataFrame(item2).T

#print(df1+200)   #200을 df1의 개수만큼 복제를 해서 연산


#존재하지 않는 인덱스의 결과는 NAN(None과는 조금 다름)
# print(df1+df2)

# #한쪽에만 존재하는 인덱스에 기본값을 설정해서 연산을 수행
# print(df1.add(df2,fill_value=0))

# #Series와 연산할 때 axis=0을 설정하면 행 단위로 연산을 수행합니다.
# print(df1.add(df2, axis=0))

###기술 통계 함수
#auto-mpg.csv 파일을 읽어서 DataFrame만들기
mpg = pd.read_csv("./data/auto-mpg.csv",header=None)
mpg.columns =['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

#print(mpg.head)
#mpg.info()

#하나의 항목 평균
# print(mpg['mpg'].mean())

# print(mpg[['mpg']].mean())   # 열 이름을 출력하고 싶을 때 일부러 하는 것임!!

#두개 항목의 평균
#print(mpg[['mpg','weight']].mean())


#문자열의 평균을 구하려고 해서 에러
# print(mpg['horsepower']..mean())

#무의미한 컬럼의 기술 통계가 같이 구해짐
mpg['origin']=mpg['origin'].astype('str')
#print(mpg.describe())


#상관계수와 공분산
# print(mpg[['mpg','cylinders','displacement']].corr())  #모든 숫자 컬럼의 상관 계수를 조회
# #모든 숫자 컬럼의 상관 계수를 조회

# print(mpg.head())

# print(mpg.sort_values(by=['mpg'],ascending=[False]))

#mpg 순으로 오름차순 정렬하고 동일한 값인 경우 displacement의 오름차순 정렬
#print(mpg.sort_values(by=['mpg','displacement'],ascending=[True,True]))


#동일한 값은 순위의 평균
# print(mpg.rank())

#동일한 값은 낮은 순위를 부여
#print(mpg.rank(method='min'))

### 데이터 시각화
### 데이터 시각화의 필요성

#앤스콤 데이터 가져오기
import seaborn as sns
anscombe = sns.load_dataset("anscombe")
#print(anscombe.head())
#print(anscombe['dataset'].unique())

#dataset 별로 분리
dataset_1= anscombe[anscombe['dataset']=='I']
dataset_2=anscombe[anscombe['dataset']=='II']
dataset_3=anscombe[anscombe['dataset']=='III']
dataset_4=anscombe[anscombe['dataset']=='IV']
'''
print(dataset_1['x'].mean())
print(dataset_2['x'].mean())
print(dataset_3['x'].mean())
print(dataset_4['x'].mean())

print(dataset_1['x'].std())
print(dataset_2['x'].std())
print(dataset_3['x'].std())
print(dataset_4[['x','y']].corr())



#데이터 시각화
import matplotlib.pyplot as plt
fig=plt.figure()

axes1=fig.add_subplot(2,2,1)
axes2=fig.add_subplot(2,2,2)
axes3=fig.add_subplot(2,2,3)
axes4=fig.add_subplot(2,2,4)

axes1.plot(dataset_1['x'],dataset_1['y'],'o')
axes2.plot(dataset_2['x'],dataset_2['y'],'o')
axes3.plot(dataset_3['x'],dataset_3['y'],'o')
axes4.plot(dataset_4['x'],dataset_4['y'],'o')

axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

plt.show()



###라인 그래프(꺾은선 그래프)
#엑셀파일 읽어오기
df=pd.read_excel('./data/시도_별_이동자수.xlsx',header=0)
#print(df.head())

#엑셀에서 셀 병합이 있으면 첫번째를 제외하고는 NAN으로 처리됨
#NaN 데이터를 앞의 데이터로 채우기
df=df.fillna(method='ffill')
#print(df.head())

#전출지별이 서울특별시이고 전입지별이 서울특별시가 아닌 데이터만 추출
#조건 생성
mask=(df['전출지별']=="경기도")&(df['전입지별']!="경기도")
df_seoul=df[mask]
#print(df_seoul.head())

#컬럼 제거
df_seoul.drop(['전출지별'],axis=1, inplace=True)
#print(df_seoul.head())

#전입지별이라는 컬럼 이름을 전입지로 변경
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
#print(df_seoul.head())

#전입지를 인덱스로 설정
df_seoul.set_index('전입지',inplace=True)
#print(df_seoul.head())

#인덱스가 전라남도인 데이터를 추출
sr_one=df_seoul.loc['전라남도']
#print(sr_one)

#sr_one 데이터를 가지고 라인 그래프 그리기
import matplotlib.pyplot as plt

#첫번째가 x축에 적용될 데이터
#두번째가 Y축에 적용될 데이터

plt.plot(sr_one.index, sr_one.values)
#plt.show()


###한글처리
import matplotlib.pyplot as plt

#운영체제 별 폰트 설정
from matplotlib import font_manager, rc
import platform

if platform.system()=="Darwin":
	rc('font',family="AppleGothic")
elif platform.system()=="Windows":
	font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#그래프 크기 설정 -단위는 inch
plt.figure(figsize=(14,5))


#x축 눈금 라벨 회전
plt.xticks(size=10, rotation='vertical')
#제목설정
plt.title('서울->전라남도',size=30)

plt.bar(sr_one.index,sr_one,width=1.0)

#라일그래프 출력
plt.plot(sr_one.index,sr_one.values,marker='p',markersize=10)
#축제목 설정
plt.xlabel('기간',size=20)
plt.ylabel('이동 인구수',size=20)

#범례
plt.legend(labels=['서울->전라남도'],loc='best',fontsize=15)
#plt.show()



###히스토그램
#히스토그램을 그릴 데이터 가져오기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

df=pd.read_csv('./data/lovefruits.csv',encoding='cp949')

#선호 과일 컬럼의 빈도수 추출
data=df['선호과일'].value_counts(sort=False)
#막대 그래프로 빈도수 출력(직접 빈도수를 구해서 그려야 합니다.)
plt.bar(range(0, len(data),1),data)
plt.xticks(range(0,len(data)))

#히스토그램 그리기 (hist 메서드가 직접 빈도수를 구해서 그려줍니다.)
plt.hist(df['선호과일'])

#plt.show()

###산포도: 데이터의 분포나 상관 관계를 파악하기 위해서 그립니다.

mpg = pd.read_csv("./data/auto-mpg.csv",header=None)
mpg.columns =['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

size=mpg['cylinders']/mpg['cylinders'].max()*200
plt.scatter(x=mpg['weight'],y=mpg['mpg'], s=size,c='coral',alpha=0.5)

#plt.show()

###seaborn
#회귀에서 사용하는 데이터 셋 가져오기
import seaborn as sns
tips=sns.load_dataset("tips")
#print(tips.head())

# 산점도와 회귀선 출력
plt.figure(figsize=(8,6))  #캔버스 크기 설정

#hue에 카테고리를 설정하면 
sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips)

#plt.show()


##히트맵 그릭
flights=sns.load_dataset('flights')
#print(flights)
#print(flights.pivot(columns=("month","year","passengers")))

#index를 month로 column에 year를 passenger의 합계를 구하는 피벗을 생성
data=flights.pivot(index="month",columns="year",values="passengers")
#print(data)

# #히트맵을 출력하는데 값을 레이블로 설정하고 포맷은 정수
# sns.heatmap(data, annot=True)
# #plt.show()


# ###데이터의 분포를 확인하기 위한 그래프
# tips=sns.load_dataset('tips')
# #print(tips)
# #sns.boxplot(x='day',y='total_bill',data=tips)
# #plt.show()

# #바이올린 플롯 - 데이터의 밀집 형태를 두께로 표시
# sns.violinplot(x='day',y='total_bill',data=tips)
# plt.show()

# sns.reset_defaults()
# sns.pairplot(tips[["total_bill","tip","size"]])
# plt.show()

'''


#plotnine
import plotnine
df=pd.DataFrame({
	'letter':['Alpha','Beta','Delta','Gamma'] *2,
	'pos':[1,2,3,4]*2,
	'num_of_letters':[5,4,5,5]*2
})

#print((plotnine.ggplot(df)+plotnine.geom_col(plotnine.aes(x='letter',y='pos',fill='letter'))+plotnine.geom_line(plotnine.aes(x='letter',y='num_of_letters',color='letter'),size=1)+plotnine.scale_color_hue(l=0.45)+plotnine.ggtitle('Greek Letter Analysis')))


###folium- 지도 출력 라이브러리

import folium

m=folium.Map(location=[37.572656,126.973300], zoom_start=15)

#마커를 찍고싶으면 
folium.Marker(location=[37.572656,126.973304], popup="KB 국민카드",icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(location=[37.554986,126.916464], popup="강남청솔",icon=folium.Icon(color='red')).add_to(m)
#지도를 html로 저장
m.save('map.html')








