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

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
symbols = [item for item in symbols if regex.search(item) == None]
#print(symbols)



start = 0
end = 500
files = []
while start < len(symbols):
    tkr = symbols[start:end]
    payload = {
            'apikey': key,
            'symbol': tkr,
            'projection': 'fundamental'
        }

    results = requests.get(url, params=payload)
    data = results.json()
    f_name = time.asctime() +'.pkl'
    f_name = re.sub('[ :]', '_', f_name)
    files.append(f_name)
    with open(f_name, 'wb') as file:
        pkl.dump(data,file)
    start = end
    end += 500
    time.sleep(1)

print(f'{len(data)}\n')
print(f'{data.keys()}\n')


