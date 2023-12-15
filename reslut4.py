import pandas as pd
s = 0
data = pd.read_csv('data.txt')
for index, row in data.iterrows():
    if row['Country'] == 'Latvia':
        if '.org' in row['Website']:
            s += 1      
print(s)