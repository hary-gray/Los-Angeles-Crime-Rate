#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import geopandas as gpd
#import contextily as ctx
#from shapely.geometry import Point

#df = pd.read_csv("Crimes in Los Angeles 2020.csv")

#gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(df.LON,df.LAT),crs='EPSG:4326')
#gdf_mercator = gdf.to_crs(epsg=3857)
#fig, ax = plt.subplots(figsize=(10,10))
#gdf_mercator.plot(ax=ax, column='Part 1-2',cmap='Set2',markersize=80,legend=True,alpha=0.8,edgecolor='black')
#ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=12)
#plt.title('Location of the Crimes in Los Angeles', fontsize=14, fontweight='bold')
#ax.set_axis_off()
#plt.tight_layout()
#plt.show()

#-------------------------------------------------------
#import contextily as ctx
#import geopandas as gpd
#import matplotlib.pyplot as plt
#import pandas as pd

# 1. Tus datos de Los Ángeles
#data = {
 #   'longitud': [-118.2437, -118.3287, -118.4124, -118.2551, -118.3617],
  #  'latitud': [34.0522, 34.0928, 34.1012, 34.0407, 34.0620],
   # 'zona': ['Downtown', 'Hollywood', 'Sherman Oaks', 'Downtown', 'Mid-Wilshire'],
    #'intensidad': [20, 35, 15, 40, 30],
#}
#df = pd.DataFrame(data)

# 2. Convertir a GeoDataFrame y reproyectar
#gdf = gpd.GeoDataFrame(
 #   df, geometry=gpd.points_from_xy(df.longitud, df.latitud), crs='EPSG:4326'
#)
#gdf_mercator = gdf.to_crs(epsg=3857)

# 3. Crear figura
#fig, ax = plt.subplots(figsize=(10, 10))

# 4. Graficar los puntos
#gdf_mercator.plot(
#    ax=ax,
#    column='zona',
#    cmap='Set2',
#    markersize=gdf_mercator['intensidad'] * 8,
#    legend=True,
#    alpha=0.85,
#    edgecolor='black',
#)

# 5. CAMBIO CLAVE: Usar CartoDB en lugar de OpenStreetMap directo
#ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite, zoom=11)

# 6. Estética final
#plt.title(
#    'Mapa de Puntos en Los Ángeles, CA', fontsize=14, fontweight='bold'
#)
#ax.set_axis_off()
#plt.tight_layout()
#plt.show()

import folium as fl
from folium.plugins import FloatImage
import pandas as pd

df = pd.read_csv("Crimes in Los Angeles 2020.csv")

map_base = fl.Map(location=[33.9513,-118.2375], zoom_start=11,tiles='Esri.WorldStreetMap')

# 3. Recorrer el DataFrame y añadir cada punto

for indice, row in df[df['AREA NAME']=='77th Street'].iterrows():
    partcolor = '#FF5733'
    if (row['Part 1-2']==2):
        partcolor = '#7A33FF'
    
    fl.CircleMarker(location=[row['LAT'],row['LON']],radius=5,color="#070606",fill=True,fill_color=partcolor,fill_opacity=0.7).add_to(map_base)


map_base.show_in_browser()