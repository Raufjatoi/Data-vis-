import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.plotting.register_matplotlib_converters()

# Load the data
data = pd.read_csv('spotify.csv', index_col='Date', parse_dates=True)
print(data.tail())

# Plot the data
plt.figure(figsize=(14,6))
sns.lineplot(data=data["Shape of You"], label="Shape of You")
sns.lineplot(data=data['Despacito'], label='Despacito')
plt.title('Daily Global Streams of Popular Songs in 2017-2018')
plt.xlabel('Dates')
plt.ylabel('Number of Streams')
plt.xticks(rotation=45)
plt.legend()
plt.show()
