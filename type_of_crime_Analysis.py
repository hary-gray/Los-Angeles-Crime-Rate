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

#Visualizing type of crimes 

df_type_crimes = df['Crm Cd Desc'].value_counts().reset_index()
#df_type_crimes['position']=np.arange(0,129,1)
df_type_crimes.sort_values(by=['count'],ascending=True,inplace=True)
df_type_crimes=df_type_crimes[df_type_crimes['count']>=2500]

fig, ax = plt.subplots(layout='constrained')
ax.barh(df_type_crimes['Crm Cd Desc'],df_type_crimes['count'])
ax.set_ylabel('Type of Crimes')
ax.set_xlabel('Amount of crimes')
ax.set_title('Type of crimes in Los Angeles in 2020')
#ax.set_xticks(df_type_crimes['position'])
#ax.tick_params(axis='x',rotation=90)


plt.show()

#print(df_type_crimes.index)