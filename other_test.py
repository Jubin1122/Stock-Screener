import pandas as pd
import re

df = pd.read_csv('nasdaq.csv')
symbols = df['Symbol'].values.tolist()

_symbols = ['AAIC^B', 'AAIC^C', 'AAL', 'AAMC', 'ABM', 'ABR^A', 'ABR^B', 'ABR^C', 'ABST', 'ABT']

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

_symbols = [item for item in _symbols if regex.search(item) == None]

print(_symbols)