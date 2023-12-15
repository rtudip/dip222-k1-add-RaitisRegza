import pandas as pd
s = 0
data = pd.read_csv('data.txt')
for index, row in data.iterrows():
    if row['Country'] == 'Latvia':   
        s += row['Number of employees']
print(s)