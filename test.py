
"""
Created by: Jubin Mohanty
Project: Ameritrade API Stock Screener
https://developer.tdameritrade.com/

"""

import configparser
import requests, time, re
import pandas as pd
import pickle as pkl

config = configparser.ConfigParser()
config.read_file(open('keys.cfg'))

key = config.get('invest22', 'apiKey')
url = config.get('invest22', 'url')

df = pd.read_csv('nasdaq.csv')
symbols = df['Symbol'].values.tolist()
#print(symbols)

print(f'The url:{url}\n')

start = 0
end = 500
files = []

while start < len(symbols):
    tickers = symbols[start:end]

    payload = {
    'apikey': key,
    'symbol': tickers,
    'projection': 'fundamental'
}

    results = requests.get(url, params=payload)
    data = results.json()

    start = end
    end += 500
"""
    f_name = time.asctime() + '.pkl'
    f_name = re.sub('[ :]', '_', f_name)
    files.append(f_name)
    with open(f_name, 'wb') as file:
        pkl.dump(data, file)




    time.sleep(1)

data = []

for file in files:
    with open(file, 'rb') as f:
        info
    
"""

print(data.keys())


