import boto3
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import json
import os.path


ts = TimeSeries(key='URYRAQZOCM9WBDO6', output_format='json')

print (os.path.abspath(boto3.__file__))

stocks=['AAPL','AXP','BA','CAT','CSCO','CVX','KO',
        'XOM','GE','GS','HD','IBM','INTC','JNJ',
        'JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG',
        'TRV','UNH','UTX','V']

# for i in stocks:
#     data, meta_data = ts.get_daily(symbol=i, outputsize='full')
#     print(i,":", data, "\n")
#     with open('../json/'+i+'.json', 'w') as txtfile:
#         json.dump(data, txtfile)

# Let's use Amazon S3/ Create an S3 client
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

#bucket = s3.Bucket('aula1ayres')
filename = '../json/teste.json'

bucket_name = 'testeproj'
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
for i in stocks:
    filename = '../json/'+i+'.json'
    s3_client.upload_file(filename, bucket_name, i+'json')
print("upload done")
