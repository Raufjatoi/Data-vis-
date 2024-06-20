import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv("iris.csv" , index_col="Id")
print(data.head())

#sns.histplot(data["Sepal Length (cm)"])
#plt.show()

#sns.kdeplot(data = data["Sepal Length (cm)"] , fill=True)
#plt.show()

#sns.jointplot(x = data["Sepal Length (cm)"] , y = data["Petal Width (cm)"] , kind='kde')
#plt.show()

#sns.histplot(data=data , x = 'Sepal Length (cm)' , hue='Species')
#plt.title("Histogram of Sepal Lenths by Species ")
#plt.show()

sns.kdeplot(data=data , x = "Petal Length (cm)" , hue = "Species" , fill=True) 
plt.title("Histogram of Petal Lenths by Species ")
plt.show()