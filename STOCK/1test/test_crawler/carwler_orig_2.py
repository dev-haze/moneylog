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
