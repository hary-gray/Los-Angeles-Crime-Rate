import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

df = pd.read_csv('Crimes in Los Angeles 2020.csv') #reading the csv file

#formating date and time columns
df['Date Rptd'] = pd.to_datetime(df['Date Rptd']) 
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])

#creating a pivot table to get the total of crimes per area and type of crime
df_topfive = df.pivot_table(values='DR_NO',index='AREA NAME', columns='Crm Cd Desc',aggfunc="count")

#filling the NA vakues
df_topfive = df_topfive.fillna(0)

#calculating the total per row to sort it from higest to lowest
df_topfive['Total']=df_topfive.sum(axis=1)
df_topfive.sort_values(by='Total',ascending=False,inplace=True)

#dropping the total culumn to transpose it and repeat the process with the other axi of the table
df_topfive.drop('Total', axis=1, inplace=True)
df_topfive = df_topfive.T
df_topfive['Total']=df_topfive.sum(axis=1)
df_topfive.sort_values(by='Total',ascending=False,inplace=True)
df_topfive.drop('Total',axis=1, inplace=True)

#filtering the top five rows
df_topfive = df_topfive.head(5)
df_topfive = df_topfive.T

#Plotting all the types of crimes vs the Area
ax=df_topfive.plot()
ax.tick_params('x',rotation=45)
ax.set_ylabel('Total of crimes')
ax.legend(title='Type of crime')
ax.set_xticks(np.arange(0,21,1),df_topfive.index)

plt.show()

#print(df_topfive.index)
#Analysis: After analyzing crime occurrences in Los Angeles in 2020, an initial finding is that vehicle theft was the most frequently reported crime, 
#with particularly high concentrations in the 77th Street and Newton areas.
#Additionally, crimes such as vandalism and felony offenses occurred consistently across the city, indicating that these 
# types of incidents were not limited to specific geographic areas. 