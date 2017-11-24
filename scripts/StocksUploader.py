import boto3

stocks=['AAPL','AXP','CVX','KO',
        'XOM','GE','GS','HD','IBM','INTC','JNJ',
        'JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG',
        'TRV','UNH','UTX','V']

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


bucket_name = 'stocksgenie'

for bucket in s3.buckets.all():
    print(bucket.name)


for i in stocks:
    filename = '../pandas/'+i+'.csv'
    print("uploading {}".format(i))
    s3_client.upload_file(filename, bucket_name, "stocks_data/"+i+'.csv')
print("upload done")
