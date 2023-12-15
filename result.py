import pandas as pd
data = pd.read_csv('data.txt')
filtered_data = data[data['Country'] == 'Oman']
min_founded = filtered_data['Founded'].min()
print(min_founded)