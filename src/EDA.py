import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/2021.csv')
df.drop(['Yr#', 'Gm#', 'Score', 'Inn','RoB', 'Out', 'Pit(cnt)','RBI','Play Description'], axis=1, inplace=True)
df.Pitcher = df.Pitcher.str.extract(r'^(.*?)\\')
batter_gb = df.groupby('Batter').mean()
sum_gb = df.groupby('Batter').sum()
count = df.groupby('Batter').count()
batter_gb['Total'] = count.LI
batter_gb['Total WPA'] = sum_gb.WPA
sorted_gb = batter_gb.sort_values('WPA')
sorted_total = batter_gb.sort_values('Total WPA')
ten_plus = sorted_gb[sorted_gb.Total >= 10]

pitcher_gb = df.groupby('Pitcher').mean()
pitcher_count = df.groupby('Pitcher').count()
pitcher_sum = df.groupby('Pitcher').sum()
pitcher_gb['Total'] = pitcher_count.LI
pitcher_gb['Total WPA'] = pitcher_sum.WPA
pitcher_sorted_gb = pitcher_gb.sort_values('WPA', ascending=False)

plt.scatter(pitcher_gb.Total, pitcher_gb.WPA)
plt.show()