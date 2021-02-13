import configparser
import requests, time, re
import pandas as pd
import pickle as pkl

config = configparser.ConfigParser()
config.read_file(open('keys.cfg'))

key = config.get('invest22', 'apiKey')
#url = config.get('invest22', 'url')

url = 'https://api.tdameritrade.com/v1/instruments'

print(f'The key:{key}\n')
print(f'The url:{url}\n')

df = pd.read_csv('nasdaq.csv')
symbols = df['Symbol'].values.tolist()
_symbols = ['A', 'AA', 'AACG', 'AACQ', 'AACQU', 'AACQW', 'AAIC',
 'AAL', 'AAMC', 'AAME', 'AAN', 'AAOI', 'AAON', 'AAP', 'AAPL', 'AAT', 
 'AAU', 'AAWW', 'AB', 'ABB', 'ABBV', 'ABC', 'ABCB', 'ABCL', 'ABCM', 
 'ABEO', 'ABEV', 'ABG', 'ABIO', 'ABM', 
'ABMD', 'ABNB', 'ABR', 'ABST', 'ABT']

len(_symbols)

#print(symbols)

start = 0
end = 10
#while start < len(_symbols):
tkr = _symbols[start:end]
print(tkr)
payload = {
            'apikey': key,
            'symbol': tkr ,
            'projection': 'fundamental'
        }

results = requests.get(url, params=payload)

print(results.json())
