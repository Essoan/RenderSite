import streamlit as st
import geopandas as gpd
import pydeck as pdk
import pandas as pd

st.set_page_config(page_title="Norway Counties Map (Pydeck)", page_icon="🗺️", layout="wide")

# --- Load your GeoJSON file ---
gdf = gpd.read_file("data/fylker.geojson")

# Ensure CRS is WGS84 (lat/lon)
if gdf.crs and gdf.crs.to_string() != "EPSG:4326":
    gdf = gdf.to_crs(epsg=4326)

# --- Convert the GeoDataFrame into a pydeck-friendly dataframe ---

def extract_coordinates(geometry):
    # Handles both Polygon and MultiPolygon
    if geometry.geom_type == "Polygon":
        return [list(geometry.exterior.coords)]
    elif geometry.geom_type == "MultiPolygon":
        return [list(poly.exterior.coords) for poly in geometry.geoms]
    else:
        return []

gdf["coordinates"] = gdf.geometry.apply(extract_coordinates)

# --- Build the Pydeck Layer ---
polygon_layer = pdk.Layer(
    "PolygonLayer",
    data=gdf,
    get_polygon="coordinates",
    get_fill_color="[34, 116, 165, 100]",  # blue with alpha
    get_line_color="[20, 74, 85, 255]",    # dark teal outline
    pickable=True,
    stroked=True,
    filled=True,
    extruded=False,
    wireframe=True,
    auto_highlight=True,
)

# --- Set the initial view state to center on Norway ---
# ... after loading gdf ...
centroids = gdf.geometry.centroid
latitude = centroids.y.mean()
longitude = centroids.x.mean()

view_state = pdk.ViewState(
    latitude=latitude, longitude=longitude,
    zoom=4.5, pitch=0
)

# --- Show in Streamlit ---
st.title("Norwegian Counties Map - Map from Pydeck")
st.pydeck_chart(
    pdk.Deck(
        layers=[polygon_layer],
        map_style="mapbox://styles/mapbox/outdoors-v12",
        initial_view_state=view_state,
        tooltip={"text": "{fylkesnavn}"},
        width=900,
        height=900
    )

)
