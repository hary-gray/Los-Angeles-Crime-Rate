import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Crimes in Los Angeles 2020.csv') #reading the csv file

#formating date and time columns
df['Date Rptd'] = pd.to_datetime(df['Date Rptd']) 
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])

#Analizing the nulls
#print(df.notnull().sum())
#print(df.tail(3))

#Visualizing amount of crimes per Area using a bar diagram
df_crimes_per_area = df['AREA NAME'].value_counts().reset_index()
fig, ax = plt.subplots(layout='constrained')
ax.bar(df_crimes_per_area['AREA NAME'],df_crimes_per_area['count'])
ax.tick_params(axis='x',rotation=90)
ax.set_xlabel('Area Name')
ax.set_ylabel('Total Crimes')
ax.set_title('Los Angeles Crimes per Area in 2020')
ax.set_ylim(0,14000)
plt.show()
#print(df_crimes_per_area)