import pandas
import folium
import numpy

PH=pandas.read_csv("ph.csv")
US=pandas.read_csv("uscities.csv")
mapping=folium.Map(location=[12,120],zoom_start=6,tiles="OpenStreetMap")

def population(pops):
    if pops < 1000000:
        return 'green'
    elif pops > 1000000 and pops < 2000000:
        return 'orange'
    elif pops > 2000000:
        return 'red'


fgPH=folium.FeatureGroup(name="Philippines")
for i in range(0,len(PH)):
    fgPH.add_child(folium.Marker(location=[PH.iloc[i]['lat'],PH.iloc[i]['lng']],popup=PH.iloc[i]['city'],
    icon=folium.Icon(color=population(PH.iloc[i]['population_proper']),icon='bullseye',prefix='fa')))  # -- for simple Marker
    #fgPH.add_child(folium.CircleMarker(location=[PH.iloc[i]['lat'],PH.iloc[i]['lng']],popup=PH.iloc[i]['city'],
    #tooltip=(PH.iloc[i]['population_proper']),fill_color='blue',color='red'))   # -- for CircleMarker marker

#fgUS=folium.FeatureGroup(name="United States of America")
#for i in range(0,len(US)):
#    fgUS.add_child(folium.Marker(location=[US.iloc[i]['lat'],US.iloc[i]['lng']],popup=US.iloc[i]['city'],icon=folium.Icon(color='blue')))
#mapping.add_child(fgUS)


fgBD=folium.FeatureGroup(name="Boundaries")
fgBD.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'yellow'}))


mapping.add_child(fgPH)
mapping.add_child(fgBD)
mapping.add_child(folium.LayerControl())




mapping.save("WorldMap.html")
