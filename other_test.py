import pandas as pd


df = pd.read_csv('nasdaq.csv')
symbols = df['Symbol'].values.tolist()

_symbols = ['A', 'AA', 'AACG', 'AACQ', 'AACQU', 'AACQW', 'AAIC', 'AAIC^B', 'AAIC^C', 'AAL', 'AAMC', 'AAME', 'AAN', 'AAOI', 'AAON', 'AAP', 'AAPL', 'AAT', 'AAU', 'AAWW', 'AB', 'ABB', 'ABBV', 'ABC', 'ABCB', 'ABCL', 'ABCM', 'ABEO', 'ABEV', 'ABG', 'ABIO', 'ABM', 
'ABMD', 'ABNB', 'ABR', 'ABR^A', 'ABR^B', 'ABR^C', 'ABST', 'ABT']

print(len(_symbols))

