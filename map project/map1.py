import folium
import pandas
def elerange(el):
    if el>=3000:
        return "red"
    elif el>=1000 and el<3000:
        return "orange"
    else:
        return "green"

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location=[40,-99], zoom_start=6)
fg = folium.FeatureGroup(name= "mera map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) +" m", radius= 6, fill_color= elerange(el), color="grey", fill_opacity= 0.7))

fg.add_child(folium.GeoJson(data= open("115 world.json", "r", encoding="utf-8-sig").read(),
style_function= lambda x: {"fillColor": "green" if x['properties']['POP2005']< 10000000 else "orange" if 10000000<=x['properties']['POP2005'] <20000000
else "red"}))

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("map1.html")
