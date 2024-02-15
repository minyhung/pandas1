import numpy as np
import pandas as pd

#클립보드의 내용을 읽어오기
#df=pd.read_clipboard()
#print(df)


#사이킷 런(scikit-learn) 에서 제공하는 데이터를 사용
from sklearn import datasets
'''
#iris 데이터 읽어오기
iris = datasets.load_iris()
#print(iris)
#데이터프레임이 아니고 Bunch 클래스의 인스턴스
print(type(iris))

#키확인
#data가 피처. target이 레이블
print(iris.keys())

#데이터확인
print(type(iris.data))

#fwf 파일 읽기
df=pd.read_fwf('C:\\Users\\USER\\Downloads\\data\\data\\data_fwf.txt', widths=(10,2,5),names=('날짜','이름','가격'),encoding='utf-8')

print(df)

#item.csv 파일 읽기
item= pd.read_csv("C:\\Users\\USER\\Downloads\\data\\data\\item.csv")
									
#전체 데이터를 출력
print(item)

print(item.info())

#good.csv 파일 읽기
#첫번째 행이 컬럼이름이 아니고 데이터
good= pd.read_csv("C:\\Users\\USER\\Downloads\\data\\data\\good.csv")

#전체 데이터를 출력
print(good)
#데이터프레임의 정보를 출력
print(good.info())


#good.csv 파일의 데이터를 2개씩 읽기
#이 방법의 경우는 데이터의 개수를 알거나 예외처리를 해주어야 합니다.

for i in range(0,3):

	parser= pd.read_csv("C:\\Users\\USER\\Downloads\\data\\data\\good.csv",
									header=None, nrows=2, skiprows=i*2)

	print(parser)

i=0
while True:
	try:
		parser= pd.read_csv("C:\\Users\\USER\\Downloads\\data\\data\\good.csv",
									header=None, nrows=2, skiprows=i*2)
		print(parser)
		i=i+1
	except:
		break


#데이터를 2개씩 읽기
parser= pd.read_csv("C:\\Users\\USER\\Downloads\\data\\data\\good.csv",
									header=None, chunksize=2)
	
for piece in parser:
	print(piece)

#탭으로 구분된 파일 읽기

gapminder= pd.read_csv("C:\\Users\\USER\\Downloads\\data\\data\\gapminder.tsv",sep='\t')
print(gapminder.head())
'''
'''
anyang=pd.read_csv("C:/Users/USER/Downloads/안양시.csv", encoding='cp949')
print(anyang.head())
#print(anyang)



jeju=pd.read_csv("C:/Users/USER/Downloads/jeju.csv", encoding='cp949')
print(jeju.head())
print(jeju)
'''

#data.to_csv('test.csv',index=False)
'''
#엑셀 파일 읽기
df=pd.read_excel('./data/excel.xlsx',sheet_name='Sheet1')
print(df.info())
print(df)

writer=pd.ExcelWriter("sample.xlsx",engine='xlsxwriter')
#엑셀 파일에 바로 기록하는 것이 아니고 임시파일에 기록을 합니다.
df.to_excel(writer, sheet_name="excel")
#파일을 닫을 때 임시 파일의 내용을 원본파일에 기록을 합니다.
#flush한다라고 표현합니다. 
writer.close()



# Retrieve the HTML data from the Korean Wikipedia page and parse it into a list of DataFrames
li = pd.read_html('https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B5%AC%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D')

print(li[0])


import urllib.request

#한글을 인코딩
from urllib.parse import quote
kw=quote("방탄소년단")

result=urllib.request.urlopen("https://search.hani.co.kr/search?searchword="+kw)
print(result.read())



import requests
param={"id":"itstudy", "name":"민형","age":27}
resp=requests.post('http://httpbin.org/post',data=param)
print(resp.text)

#이미지 파일 다운로드
imageurl="https://www.ascentkorea.com/wp-content/uploads/2022/11/bts.jpg"

#저장할 파일 이름
filename="bts.jpg"

try:
	#다운로드
	resp=requests.get(imageurl)
	#파일에 저장
	with open(filename, "wb") as h:
		img=resp.content
		#파일에 저장
		h.write(img)
except Exception as e:
	print(e)

df=pd.read_json("http://swiftapi.rubypaper.co.kr:2029/hoppin/movies?version=1&page=1&count=30&genreId=&order=releasedateasc")
#print(type(df))
hoppin=df["hoppin"]
movies=hoppin['movies']
#print(movies)

movie=movies["movie"]
#print(movie)

for item in movie:
	print(item["title"]+":"+item["ratingAverage"])
'''

#kakao Open Api 데이터 가져오기
import requests
import json

#url 만들기
url = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=PM9&rect=126.95,37.55, 127.0, 37.60'

#헤더설정
headers={'Authorization': 'KakaoAK {}'.format('3449e6f606f172baa412b7235d1ba199')}

#데이터를 다운로드
data=requests.post(url, headers=headers)
#다운로드 받은 문자열을 확인
#print(data.text)

#JSON문자열을 Python 의 자료구조로 변경
result=json.loads(data.text)
#print(type(result))

#documents 키의 데이터를 가져오기
documents = result['documents']
#print(documents)

for doc in documents:
	print(doc['place_name'],doc['address_name'])

import pymysql

con = pymysql.connect(host="localhost", port=3306, user="root", passwd="wnddkd", db="hyung", charset="utf8")

#테이블 생성 구문 실행

#SQL을 실행하기 위한 객체 생성
cursor=con.cursor()
#cursor.execute("create table pharmacy(placename char(30),addressname varchar(200))")

#파싱한 데이터 순회
for doc in documents:
	cursor.execute("insert into pharmacy(placename, addressname) values(%s, %s)", (doc["place_name"],doc["address_name"]))

con.commit()

#print(con)
con.close()

#한겨레 rss 파싱
import urllib.request
import xml.etree.ElementTree as etr

# 데이터 읽어오기
url = "https://www.hani.co.kr/rss/sports"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')  # 바이너리 데이터를 문자열로 디코딩

# XML 파싱
tree = etr.ElementTree(etr.fromstring(data))
xroot = tree.getroot()
print(xroot)


import requests
import bs4

resp=requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")
html=resp.text
print(html)


#html파싱
bs = bs4.BeautifulSoup(html,'html.parser')
#html에서 body 태그 안의 span 태그의 텍스트를 가져오기

cities=[]
temp=[]
tags=bs.select('th > a')
for tag in tags:
	cities.append(tag.getText())
tags=bs.select('td:nth-child(6)')
for tag in tags:
	temp.append(tag.getText())

for i in range(0,11):
	print(cities[i]+ ":"+ temp[i])






