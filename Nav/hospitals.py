import streamlit as st
import folium
from streamlit_folium import st_folium

# Function to create and display a map
def hospital():
    st.write("Find Hospital Through Map")
    # Create a folium map centered at a specific location
    center_location = [37.7749, -122.4194]  # Example coordinates (San Francisco)
    m = folium.Map(location=center_location, zoom_start=12)

    # Add a marker to the map
    folium.Marker(
        location=center_location,
        popup="San Francisco",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)
