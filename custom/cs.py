import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv('spotify.csv' , index_col='Date' , parse_dates=True)

sns.set_style('darkgrid')
plt.figure(figsize=(12,6))
sns.lineplot(data=data)
plt.show()