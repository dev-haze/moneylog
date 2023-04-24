import FinanceDataReader as fdr

df_krx = fdr.StockListing("KRX")

df_head = df_krx.head(20)
print(df_head)



for comp in df_krx:
    print(comp)
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    


df_spx = fdr.StockListing("KRX")




class Data_searcher:
    def __init__(self):
        df_krx = fdr.StockListing("KRX")
