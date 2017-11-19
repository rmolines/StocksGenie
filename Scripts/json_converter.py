import os.path

stocks=['AAPL','AXP','CVX','KO',
        'XOM','GE','GS','HD','IBM','INTC','JNJ',
        'JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG',
        'TRV','UNH','UTX','V', 'GOOG', 'MSFT']

j = 0;
for i in stocks:
    j += 1;
    print("loading...")
    data, meta_data = ts.get_daily(symbol=i, outputsize='full')
    print("ticker: ")
    print(i)
    with open('../json/'+i+'.json', 'r') as txtfile:
        with open('../pandas/'+i+'.pandas', 'w') as wfile:
            data.to_csv(txtfile, sep='\t', encoding='utf-8')
