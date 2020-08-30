#Importing libraries for reading & Visualization
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

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

#Changing the value to time series from object type
data_set["Date"]=pd.to_datetime(data_set['Date'])
data_set=data_set.sort_values("Date")

#Printing the datatypes 
print(data_set.dtypes)

#Time Series
time_series=data_set[['Date','Rating', 'Category']]
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

#Vizualizing the plotting of graph
y.plot(figsize=(20,10))
plt.show()

# time_series Decomposition
# from pylab import rcParams
# rcParams['decomp_figsize']= 18,9

# decomposition=sm.tsa.seasonal_decompose(y, model='additive')
# fig = decomposition.plot()
# plt.show() 

#Star Ratings
data_highstars=data_set.groupby("Rating").agg({'Rating':'count'})
data_highstars.rename({'Rating':'No. of ratings'},axis=1,inplace=True)
data_highstars.plot(kind="line")

#Star Ratings
data_highstars=data_set.groupby("Rating").agg({'Rating':'count'})
data_highstars.rename({'Rating':'No. of ratings'},axis=1,inplace=True)
data_highstars.plot(kind="bar")

#Free and paid 
free_apps=data_set.groupby("Price").agg(sum).sort_values("Price",ascending=True)
free_apps.plot(kind="bar",figsize=(20,10))

##As you can see clearly we aren't able to see graph clearly so plotting for only paid 
paid_apps=free_apps.loc[(free_apps["Rating"]<25) & (free_apps["People(no.)"]<50000)]
paid_apps.plot(kind="bar", figsize=(20,10))

















