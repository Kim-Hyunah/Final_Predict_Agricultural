from urllib.request import urlopen 
from urllib.parse import urlencode, unquote, quote_plus
import urllib 
import requests 
import json 
import pandas as pd 

# Setting for URL parsing 
url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
enKey = "RV5qrbJRiVSlbKPN32nnD3kFJt1g%2BTluv17SHOslrqUvunmsT0BuEKZluh0doSFS7SAYLR4U4O6Sn14uhN4wdA%3D%3D"

params = f'?{quote_plus("ServiceKey")}={enKey}&' + urlencode({ 
    quote_plus("pageNo"): "1", # 페이지 번호 // default : 1 
    quote_plus("numOfRows"): "10", # 한 페이지 결과 수 // default : 10 
    quote_plus("dataType"): "JSON", # 응답자료형식 : XML, JSON 
    quote_plus("dataCd"): "ASOS",
    quote_plus("dateCd"): "HR",
    quote_plus("startDt"): "20181229", 
    quote_plus("startHh"): "01",
    quote_plus("endDt"): "20191130",
    quote_plus("endHh"): "01",
    quote_plus("stnIds"): "108"
    })

# # URL parsing 
# req = urllib.request.Request(url + params)

# # Get Data from API 
# response_body = urlopen(req).read()   # get bytes data 
# print(response_body)
# # # Convert bytes to json 
# data = json.loads(response_body) 
# print(data)

data = requests.get(url + params).json()

# Result 
res = pd.DataFrame(data['response']['body']['items']['item'])
print(res)