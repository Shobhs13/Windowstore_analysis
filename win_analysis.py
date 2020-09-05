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
paid_apps=paid_apps.drop(columns="People(no.)")
paid_apps.plot(kind="line", figsize=(20,10))

#categorical value
cat_val=data_set.groupby("Category")["Rating"].agg([np.max,np.min,np.mean])
cat_val.plot(kind="bar", rot=45, figsize=(20,10))

#Getting the paid apps, category values
pai_cat=data_set[["Name","Category","Price"]].copy()
pai_cat.rename({'Price':'Price in Rs.'}, axis=1, inplace=True)
pai_cat=pai_cat.loc[pai_cat["Price in Rs."]!="Free"]
pai_cat_val=pai_cat.groupby("Category").agg({"Category":"count"})
pai_cat_val.plot(kind="bar", rot=45)

# columns
print(data_set.columns)

#Category wise the best apps in different domains
cat_tech_paid=data_set.loc[(data_set["Category"]=="Developer Tools") & (data_set["Price"]!="Free")].sort_values("Rating",ascending=False)

#CLeaning the columns for plotting
import re
cat_tech_paid['Price'] = cat_tech_paid['Price'].str.replace('\₹', '')
cat_tech_paid.plot("Name","Rating",kind="bar",figsize=(20,10),title="Rating vs Paid Apps")
cat_tech_paid_rat=cat_tech_paid.groupby("Rating").agg(sum)
cat_tech_paid_rat.plot(kind="bar",rot=45,color='green',title="No. of people vs Ratings of Developer apps")
