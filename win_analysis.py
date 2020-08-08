#Importing libraries for reading & Visualization
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

#Reading Dataframe
data_set=pd.read_csv("msft.csv", encoding="UTF-8")
print(data_set)

print(data_set.columns)

#Describing the dataframe
print(data_set.describe())

#Renaming the dataframe
data_set.rename({'No of people Rated':'People(no.)'}, axis=1, inplace=True)
print(data_set)

#no of reviews day wise
data_group=data_set.groupby(['Date', 'Rating','People(no.)']).sum().reset_index()
print(data_group)
data_group=data_group.sort_values("Date", axis=0, ascending=True)

df_category=data_set.groupby(['Name','Category','Price']).sum().sort_values("Category", ascending=True)
print(df_category.head())

#Finding the apps which are not free
data_notfree=data_set.loc[data_set["Price"]!="Free"]     

