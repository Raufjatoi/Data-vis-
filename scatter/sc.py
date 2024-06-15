import pandas as pd 
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv('insurance.csv')

#sns.scatterplot(x=data['bmi'], y=data['charges'])
#sns.regplot(x=data['bmi'], y=data['charges'])
#sns.scatterplot(x=data['bmi'], y=data['charges'] , hue=data['smoker'])
sns.lmplot(x="bmi", y="charges", hue="smoker", data=data)
#sns.swarmplot(x=data['bmi'], y=data['charges'])
plt.show()