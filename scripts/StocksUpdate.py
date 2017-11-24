import boto3
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import json
import os.path
import pandas as pd


ts = TimeSeries(key='URYRAQZOCM9WBDO6', output_format='pandas')

print (os.path.abspath(boto3.__file__))

stocks=['AAPL','AXP','CVX','KO',
        'XOM','GE','GS','HD','IBM','INTC','JNJ',
        'JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG',
        'TRV','UNH','UTX','V']


j = 0;
for i in stocks:
    j += 1;
    print("loading...")
    data, meta_data = ts.get_daily(symbol=i, outputsize='full')
    print("ticker: ")
    print(i)
    print(len(data))
    df = pd.DataFrame(data, columns=None)
    df['ticker'] = i
    with open('../pandas/'+i+'.csv', 'w') as txtfile:
        df.to_csv(txtfile, header=False)
