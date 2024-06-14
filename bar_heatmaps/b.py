import pandas as pd 
pd.plotting.register_matplotlib_converters
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv('flight_delays.csv' , index_col='Month')

#print(data)

plt.figure(figsize=(10, 6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

sns.barplot(x=data.index , y=data['NK'])
plt.ylabel('Arrival delay (in minutes )')
#plt.show()

plt.figure(figsize=(14,7))

plt.title("Average Arrival Delay for Each Airline, by Month")
sns.heatmap(data=data , annot=True)
plt.xlabel("Airline")
plt.show()
