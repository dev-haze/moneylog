import requests
from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self):
        self.ls_code=[]#코드
        self.ls_price=[]#가격
        self.ls_total = []#시가총액
        self.ls_auth=[]#발행주식수
        
        self.ls_PBR=[]
        self.ls_PER=[]
        self.ls_EPS=[]
        self.ls_BPS=[]
        #상장주식수, 시가총액,

        self.url = "https://finance.naver.com/item/main.nhn?code="
        

        #태그 가져오기
        self.df_m = saveNload()
        self.df = self.df_m.load()
        self.ls_tag = self.df.iloc[:,0]
        print(self.ls_tag)
        del self.ls_tag[0]




'''
<시뮬레이션>

-투자전략1
1.분기보고서 나오는 달 말일에 PBR||PER 가장 낮은 순으로 코스피200정렬하고 하위 20종목 뽑기
2. 다음분기, 분기보고서 나오는 달 말일에 이전 분기에 매수한 주식 매도. 같은날에 1번 방법으로 매수




자산 = 자본+부채


'''


