import streamlit as st
import geopandas as gpd
import pydeck as pdk
from matplotlib import cm
import numpy as np

st.set_page_config(page_title="Norway Counties Map (Pydeck)", page_icon="🗺️", layout="wide")

# --- Cache loading and prepping GeoJSON with dynamic colors ---
@st.cache_data
def load_and_prepare_gdf(path):
    gdf = gpd.read_file(path)
    # Ensure CRS is WGS84 (lat/lon)
    if gdf.crs and gdf.crs.to_string() != "EPSG:4326":
        gdf = gdf.to_crs(epsg=4326)
    # Assign a unique color to each county (fylkesnavn)
    county_names = gdf["fylkesnavn"].unique()
    n_colors = len(county_names)
    cmap = cm.get_cmap("tab20", n_colors)
    color_dict = {name: [int(255*r), int(255*g), int(255*b), 120]
                  for name, (r, g, b, _) in zip(county_names, cmap(np.linspace(0, 1, n_colors)))}
    gdf["fill_color"] = gdf["fylkesnavn"].map(color_dict)

    # Extract coordinates for pydeck
    def extract_coordinates(geometry):
        if geometry.geom_type == "Polygon":
            return [list(geometry.exterior.coords)]
        elif geometry.geom_type == "MultiPolygon":
            return [list(poly.exterior.coords) for poly in geometry.geoms]
        else:
            return []
    gdf["coordinates"] = gdf.geometry.apply(extract_coordinates)
    return gdf

gdf = load_and_prepare_gdf("data/fylker.geojson")

# --- Cache the entire pydeck map object (for speed!) ---
@st.cache_data
def build_deck(_gdf):
    polygon_layer = pdk.Layer(
        "PolygonLayer",
        data=gdf,
        get_polygon="coordinates",
        get_fill_color="fill_color",
        get_line_color="[40,40,40,200]",
        pickable=True,
        stroked=True,
        filled=True,
        extruded=False,
        wireframe=True,
        auto_highlight=True,
    )
    # Center on Norway
    centroids = gdf.geometry.centroid
    latitude = centroids.y.mean()
    longitude = centroids.x.mean()
    # --- Center and fit tightly to Norway ---
    bounds = gdf.total_bounds  # [minx, miny, maxx, maxy]
    center_lat = (bounds[1] + bounds[3]) / 2
    center_lon = (bounds[0] + bounds[2]) / 2

    view_state = pdk.ViewState(
        latitude=center_lat,
        longitude=center_lon,
        zoom=5.2,  # Try 5.5, 5.7, etc for tighter view
        pitch=0,
        bearing=0
    )

    deck = pdk.Deck(
        layers=[polygon_layer],
        map_style="mapbox://styles/mapbox/outdoors-v12",
        initial_view_state=view_state,
        tooltip={"html": "<b>Fylke:</b> {fylkesnavn}", "style": {"backgroundColor": "steelblue", "color": "white"}}
    )
    return deck

deck = build_deck(gdf)

st.title("Norwegian Counties Map - Dynamic Colors (Pydeck)")
st.pydeck_chart(deck, width=750, height=750)
