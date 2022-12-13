# 배추 생산량 예측

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

encoding = "RV5qrbJRiVSlbKPN32nnD3kFJt1g%2BTluv17SHOslrqUvunmsT0BuEKZluh0doSFS7SAYLR4U4O6Sn14uhN4wdA%3D%3D"
decoding = "RV5qrbJRiVSlbKPN32nnD3kFJt1g+Tluv17SHOslrqUvunmsT0BuEKZluh0doSFS7SAYLR4U4O6Sn14uhN4wdA=="

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=encoding&numOfRows=10&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=20100101&endDt=20100102&stnIds=108"
