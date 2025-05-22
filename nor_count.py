import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# 1. Load your MultiPolygon GeoJSON
norway_gdf = gpd.read_file("data/fylker.geojson")

# 2. Convert all non-serializable columns to string
for col in norway_gdf.columns:
    if str(norway_gdf[col].dtype).startswith("datetime"):
        norway_gdf[col] = norway_gdf[col].astype(str)

# 3. Get the centroid for the initial map focus (this works for MultiPolygons too)
centroid = norway_gdf.geometry.centroid.iloc[0]
lat, lon = centroid.y, centroid.x

# 4. Create the Folium map
m = folium.Map(location=[lat, lon], zoom_start=5)

# 5. Add the MultiPolygon GeoDataFrame as a GeoJson layer
folium.GeoJson(
    norway_gdf,
    name="Norway",
    style_function=lambda feature: {
        'fillColor': '#2274A5',
        'color': '#144A55',
        'weight': 2,
        'fillOpacity': 0.35,
    }
).add_to(m)

# 6. Display the map in Streamlit
st.title("Norway MultiPolygon Map (Folium + Streamlit)")
st_folium(m, width=700, height=500)
