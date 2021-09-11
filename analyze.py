import pandas as pd
import numpy as np  
import re
import matplotlib.pyplot as plt
from pyvis.network import Network
bod = pd.read_csv('bod.csv', index_col =[0])
bod.columns
company = pd.read_csv('company_list.csv', index_col=[0])
company.head(10)
bod.drop_duplicates(subset = ['Name', 'YearOfBirth', 'StockCode'],keep = False, inplace=True)
bod['Name'] = bod.apply(lambda x: re.sub(r'(^\w{2,3}\. ?)', r'', x['Name']),axis=1)

#Group by to attach id to individuals
bod_agg = bod.groupby(by=['Name','YearOfBirth'])['StockCode'].count().reset_index()
bod_agg[bod_agg['StockCode']>4].sort_values(by='StockCode',ascending=False)
bod_agg['id'] = bod_agg.index
bod_agg = bod_agg[bod_agg['StockCode']>1]
#Left join id to intial table
edge = bod.merge(bod_agg[['Name','YearOfBirth','id']],
                    how='inner', 
                    left_on=['Name','YearOfBirth'], 
                    right_on=['Name','YearOfBirth'])[['id','StockCode']]
edge.StockCode.describe()

def map_data():
    g = Network(height='1500px',width ='100%',bgcolor='#222222',font_color='white')
    for index, row in bod_agg.iterrows():
        if row['StockCode'] >=5:
            g.add_node(row['id'], label =row['Name']+','+str(row['YearOfBirth']), color='purple',size=150)
        else:
            g.add_node(row['id'], label =row['Name'])
    for index, row in edge.iterrows():
        g.add_node(row['StockCode'], color ='#DED007')
        g.add_edge(row['StockCode'],row['id'])
    g.barnes_hut()
    g.show("result.html")

map_data()


