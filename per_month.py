import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Crimes in Los Angeles 2020.csv") #read the csv file

df['DATE OCC'] = pd.to_datetime(df['DATE OCC']) #set date format
df['Date Rptd'] = pd.to_datetime(df['Date Rptd']) #set date format

df_pivot = df.pivot_table(values='DR_NO', index=df['DATE OCC'].dt.to_period('M'), columns='Crm Cd Desc', aggfunc='count') #pivot table date vs type of crime
#print(df_pivot)
df_pivot = df_pivot.T # organize the pivot table to filter the top five
df_pivot['Total'] =df_pivot.sum(axis=1)
df_pivot.sort_values(by='Total',ascending=False,inplace=True)
df_pivot = df_pivot.head(5)
df_pivot.drop(columns='Total',inplace=True)
df_pivot = df_pivot.T

df_pivot1 = df.pivot_table(values='DR_NO', index=df['DATE OCC'].dt.to_period('M'), columns='AREA NAME', aggfunc='count') #pivot table for Zones
#print(df_pivot)
df_pivot1 = df_pivot1.T
df_pivot1['Total'] =df_pivot1.sum(axis=1)
df_pivot1.sort_values(by='Total',ascending=False,inplace=True)
df_pivot1 = df_pivot1.head(5)
df_pivot1.drop(columns='Total',inplace=True)
df_pivot1 = df_pivot1.T


fig, ax = plt.subplots(2,layout='constrained') #plotting both tables

df_pivot.plot(ax=ax[0])
df_pivot1.plot(ax=ax[1])
ax[0].set_xticks(np.arange(0,12,1),df_pivot1.index)
ax[1].set_xticks(np.arange(0,12,1),df_pivot1.index)


plt.show()

#print(df_pivot)
