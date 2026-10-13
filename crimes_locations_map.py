import folium as fl
import pandas as pd

df = pd.read_csv("Crimes in Los Angeles 2020.csv")

map_base = fl.Map(location=[33.9513,-118.2375], zoom_start=13,tiles='Esri.WorldStreetMap')

# 3. Recorrer el DataFrame y añadir cada punto

for indice, row in df[df['AREA NAME']=='77th Street'].iterrows():
    partcolor = '#FF5733'
    if (row['Part 1-2']==2):
        partcolor = '#7A33FF'
    
    fl.CircleMarker(location=[row['LAT'],row['LON']],radius=5,color="#070606",fill=True,fill_color=partcolor,fill_opacity=0.7).add_to(map_base)


map_base.show_in_browser()