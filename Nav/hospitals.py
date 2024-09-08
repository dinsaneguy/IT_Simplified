import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium
import streamlit.components.v1 as components
def hospital():
    def MapsShower():
        st.title("Leaflet Map with Custom Tile Layer")

        m = folium.Map(location=[27,85], zoom_start=7)
        folium.TileLayer(
            tiles='https://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.png',
            attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.',
            name='Stamen Terrain'
        ).add_to(m)
        
        # Add a layer control
        folium.LayerControl().add_to(m)

        # Load the CSV file with hospital data
        data = pd.read_csv('maps.csv')

        # Add markers for each hospital from the CSV file
        for index, row in data.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)

        # Display the map using streamlit-folium
        st_folium(m, width=700, height=500)
    MapsShower()