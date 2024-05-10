# Import dependencies needed to run the code
import streamlit as st
import pandas as pd
import geopandas as gpd
import pydeck as pdk


# set page configurations
st.set_page_config(
    page_title="Fulton County Housing Trends",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# map variables
starting_lat = 33.79822069509032
starting_long = -84.43576908765439

# choropleth color ramp
color_ramp = ['rgb(239,243,255)','rgb(189,215,231)','rgb(107,174,214)','rgb(49,130,189)','rgb(8,81,156)']