import requests
from bs4 import BeautifulSoup
import re






class Main:
    def __init__(self):
        self.url = "https://finance.naver.com/item/main.nhn?code="
        self.data = [][]
              

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
        pass

    

        


class Main:
    def __init__(self):
        self.ls_tag=[]
        self.ls_price=[]
        self.url = "https://finance.naver.com/item/main.nhn?code="

        self.ls_tag.append('005930')

    def get_price_one(self,tag):
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

    def get_total_one(self,tag):
        urltag = self.url + tag
        response = requests.get(urltag)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        amount = soup.select_one('#_market_sum')
        rsult = amount.get_text().replace(',','')
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

    def show(self):
        count = 1
        for each in self.ls_tag:
            code = str(each)
            for i in range(6-len(code)):
                code = "0"+code

            name = self.get_name(code)
            price = self.get_price_one(code)
            amount = self.get_amount_one(code)

            total = name,price,amount;
            self.df.loc[count,4] = total
            print("total:",total)

                   
            count+=1
            
            print(price,' ',amount,' ',total,' ',name,' ')

    

   
m = Main()
rsult = m.get_price_one('005930')
m.show()
