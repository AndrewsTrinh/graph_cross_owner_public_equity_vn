import pandas as pd
import numpy as np
import requests as rq
import time
import random

def get_company():
    url_stock_list = 'https://api-dulieu.mbs.com.vn/api/OverviewMarket/GetAutoCompleteCompany?languageId=2'
    r1= rq.get(url_stock_list)
    company = pd.DataFrame.from_dict(r1.json()['Data'], orient='columns')
    return company

def get_bod(stock_code):
    url = f'https://api-dulieu.mbs.com.vn/api/Enterprise/GetCompanyProfileCTCPBoardOfManagements?iLanguage=2&iStockCode={stock_code}'
    r = rq.get(url)
    print(r.json()['Code'])
    if len(r.json()['Data']) != 0:
        temp = pd.DataFrame(r.json()['Data'])
        temp['StockCode'] = stock_code
        return temp
    else:
        pass

def get_bod_data():
    stock_list = get_company()['CompanyCode']
    print('crawling: ',len(stock_list),' stocks')
    bod_data = pd.DataFrame()
    i = 0
    f = 0
    for stock_id in stock_list:
        print(stock_id,' start!')
        try:
            bod_data = bod_data.append(get_bod(stock_id))
            i = i+1
        except:
            f = f+1
            pass
        print(stock_id,' done! | ',i,' passed | ',f,' failed!')
        time.sleep(random.choice([0.1,0.1,0.1,1]))
    return bod_data    

bod_data =get_bod_data()
col_name = ['Name', 'Position','YearOfBirth','FromDate','stock_id']
bod_data=bod_data[col_name]
bod_data.to_csv('bod.csv')
company_list = get_company()
company_list.to_csv('company_list.csv')
