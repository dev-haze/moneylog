import requests
from bs4 import BeautifulSoup
import re

import FinanceDataReader as fdr




class Main:
    def __init__(self):
        self.url = "https://finance.naver.com/item/main.nhn?code="
        self.data = [[]]
        df_krx = fdr.StockListing("KRX")

        col_name = df_krx.columns.to_list()
        print(col_name)

        self.krx = df_krx.to_numpy()

        print('name',self.krx[0][2])
        print('amount',self.krx[0][13])
        
        #print(krx[0])
        

    def get_price_one(self, tag):
        urltag = self.url + tag
        html = requests.get(urltag)
        soup = BeautifulSoup(html.content, 'html.parser')
        html1 = soup.find('div',class_='today')
        html2 = html1.find('p',class_='no_today')
        price = html2.find_all('em',class_='no_down')
        price = html2.find_all('span',class_='blind')
        result_price = re.sub(r'[^0-9]', '', str(price))
        print("price : ",result_price)
        return result_price
    
    def get_amount_one(self,tag):
        urltag = self.url + tag
        response = requests.get(urltag)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        amount = soup.select_one('#tab_con1 > div.first > table > tr:nth-child(4) > td > em')
        rsult = amount.get_text().replace(',','')
        print("amount : ",rsult)
        return rsult

    def get_name(self,tag):
        urltag = self.url + tag
        response = requests.get(urltag)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        amount = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a')
        rsult = amount.get_text()
        print("name : ",rsult)
        return rsult

    def update_price(self):
        count=1
        for each in self.data:
            code = str(each[0])
            for i in range(6-len(code)):
                code = "0"+code
            price = self.get_amount_one(code)
                
            
            amount= self.get_amount_one(code)

            total = price*amount

            name = self.get_name(code)

            count+=1
        

    def show(self):
        for y in self.data:
            for each in y:
                print(each)
                pass

        
#code[0], name[2], close, 

   
m = Main()
rsult = m.get_price_one('005930')
m.show()
