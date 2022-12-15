import pandas as pd
import numpy as np

nc_output= pd.read_csv("data/배추_생산량.csv", encoding="utf-8")
nc_output

# 품목별로 추출
type= nc_output[nc_output["시도별"]=="품목별"]

# city 배열 생성
city = ["서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시", "대전광역시", "울산광역시", "세종특별자치시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도"]
city_list= ["seoul", "busan", "daegu", "incheon", "gwangju", "daejeon", "ulsan", "sejong", "gyeonggi", "gangwon", "chungbuk", "chungnam", "jeonbuk", "jeonnam", "gyeongbuk", "gyeongnam", "jeju"]

# city 배열과 city_list 배열을 이용하여 city별로 추출
for i in range(len(city)):
    globals()[city_list[i]] = nc_output[nc_output["시도별"]==city[i]]
    
# type과  시도별로 합치기
for i in range(len(city)):
    globals()[city_list[i]] = pd.merge(type, globals()[city_list[i]], how="outer")

year_list= np.arange(2000, 2022)
# season 배열 생성
#season = ["spring", "summer", "fall", "winter"]
# spring = 2000,2000.1,2000.2,2001,2001.1,2001.2  summer = 2000.3,2000.4,2000.5,2001.3,2001.4,2001.5  fall = 2000.6,2000.7,2000.8,2001.6,2001.7,2001.8  winter = 2000.9,2000.10,2000.11,2001.9,2001.10,2001.11
#detail = [".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11"]
spring= [".1",".2"]
summer= [".3", ".4", ".5"]
fall= [".6", ".7", ".8"]
winter= [".9", ".10", ".11"]

yr_list= np.arange(2000, 2022)
detail = [".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11"]
spring= []
summer= []
fall= []
winter= []

for yr in yr_list:
    spring.append(yr)
    for i in range(0,2):
        val= str(yr) + detail[i]
        spring.append(val)
    for i in range(2,5):
        val= str(yr) + detail[i]
        summer.append(val)
    for i in range(5,8):
        val= str(yr) + detail[i]
        fall.append(val)
    for i in range(8,11):
        val= str(yr) + detail[i]
        winter.append(val)
print(winter)

# spring_seoul = seoul안에 데이터에서 spring배열안에 있는 값만 추출 using try exepct make dataf
spring_seoul= pd.DataFrame()
for i in range(0, len(spring)):
    try:
        
    except:
        pass

spring_seoul
