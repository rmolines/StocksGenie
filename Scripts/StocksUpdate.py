import boto3
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import json
import os.path
import pandas as pd

def data_T (data):
    temp = []
    for i in range(len(data)):
        print(data[i])

ts = TimeSeries(key='URYRAQZOCM9WBDO6', output_format='pandas')

print (os.path.abspath(boto3.__file__))

stocks=['AAPL','AXP','CVX','KO',
        'XOM','GE','GS','HD','IBM','INTC','JNJ',
        'JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG',
        'TRV','UNH','UTX','V', 'GOOG']


j = 0;
for i in stocks:
    j += 1;
    print("loading...")
    data, meta_data = ts.get_daily(symbol=i, outputsize='full')
    print("ticker: ")
    print(i)
    print(len(data))
    df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close', 'volume'])
    # data_T(data)
    with open('../pandas/'+i+'.csv', 'w') as txtfile:
        df.to_csv(txtfile)
        # json.dump(data, txtfile)



# for i in stocks:
#     filename = '../json/'+i+'.json'
#
#     df = pd.read_json(filename, orient='open')
#     with open('../pandas/'+i+'.csv', 'w') as txtfile:
#         df.to_csv(txtfile, sep='\t', encoding='utf-8')
#     print("Ticker: "+ i)
#
# # Let's use Amazon S3/ Create an S3 client
# s3 = boto3.resource('s3')
# s3_client = boto3.client('s3')
#
# #bucket = s3.Bucket('aula1ayres')
# filename = '../pandas/teste.csv'
#
# bucket_name = 'testeproj'
# # Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)
#
# # Uploads the given file using a managed uploader, which will split up large
# # files automatically and upload parts in parallel.
# for i in stocks:
#     filename = '../pandas/'+i+'.csv'
#     s3_client.upload_file(filename, bucket_name, i+'csv')
# print("upload done")
