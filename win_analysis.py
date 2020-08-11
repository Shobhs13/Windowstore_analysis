#Importing libraries for reading & Visualization
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

#Reading Dataframe
data_set=pd.read_csv("msft.csv", encoding="UTF-8")
data_set=data_set.dropna()
print(data_set)

print(data_set.columns)

#Describing the dataframe
print(data_set.describe())

#Renaming the dataframe
data_set.rename({'No of people Rated':'People(no.)'}, axis=1, inplace=True)
print(data_set)

#Printing the datatypes 
print(data_set.dtypes)

#Changing the value to time series from object type
data_set["Date"]=pd.to_datetime(data_set['Date'])

#no of reviews day wise
data_group=data_set.groupby(['Date', 'Rating','People(no.)']).sum().reset_index()
print(data_group)
data_group=data_group.sort_values("Date", axis=0, ascending=True)

df_category=data_set.groupby(['Name','Category','Price']).sum().sort_values("Category", ascending=True)
print(df_category.head())

#Finding the apps which are not free
data_notfree=data_set.loc[data_set["Price"]!="Free"]  

#Sort the values by Rating.
data_set_rating=data_set.groupby(["Rating","Name","Category"]).sum().sort_values(["Rating","Category"], ascending=False)   
print(data_set_rating)

#Time Series
time_series=data_set[['Date','Name','Rating', 'Category']]
time_series['Date'].min(),time_series["Date"].max()

#Sorting the time_series column date wise
time_series=time_series.sort_values("Date")
time_series.isnull().sum()

#Grouping by date
time_series=time_series.groupby('Date')['Rating'].sum().reset_index()
time_series=time_series.set_index('Date')
print(time_series.index)

#working with the data 
y = time_series['Rating'].resample('MS').mean()
print(y["2017":])
y=y.dropna()

#Vizualizing the plooting of graph
y.plot(figsize=(20,10))
plt.show()

# time_series Decomposition
from pylab import rcParams
rcParams['decomp_figsize']= 18,9

decomposition=sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show() 










