# Import dependencies needed to run the code
import streamlit as st
import pandas as pd
import geopandas as gpd
import topojson as tp
import plotly.express as px

# set page configurations
st.set_page_config(
    page_title="Fulton County Housing Trends",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar help text
st.sidebar.write("Filter housing data by year sold")

# Provide vertical spacing
st.sidebar.write("")

# Transaction year slider
years = st.sidebar.select_slider(
    'Transaction year',
    options=[
        2018,
        2019,
        2020,
        2021,
        2022,
        2023
    ],
    value=(2021, 2023)
)

# Sidebar dropdown to change basemap
basemap_select = st.sidebar.selectbox(
    "Change basemap",
    ('Light', 'Dark'),
    index=1,
    placeholder='this is a test'
)

# Dictionary will 'translate' the basemap selection to a CartoDB tile map
basemap_dictionary = {
    'Light': 'positron',
    'Dark': 'darkmatter'
}

# # define app header, subheader
# st.header('Fulton County Home Sale Prices')
# st.subheader(
#     f'Median Price / SF by Census Tract: {years[0]} - {years[1]}', divider='blue')

# On load, read in sales data
df_sales = pd.read_csv(
    '4_JoinedSales.csv',
    dtype={
        'sale_year': 'object',
        'price_sf': 'float',
        'GEOID': 'object'
    })

# # Take a look at the data - no filter applied
# st.dataframe(df_sales, use_container_width=True)

# Define variables to hold slider values
year_lower_bound = years[0]
year_upper_bound = years[1]

# # Check slider values
# st.write(f'Slider value 1: {year_lower_bound}')
# st.write(f'Slider value 2: {year_upper_bound}')

# Now filter initial dataframe on these slider values
filtered_df = df_sales[
    (df_sales['sale_year'].astype(int) >= year_lower_bound) &
    (df_sales['sale_year'].astype(int) <= year_upper_bound)]

# # Take a look at the data - year filter applied
# st.dataframe(filtered_df, use_container_width=True)

# Now that we are properly filtering, we aggregate the sales by Census tract
agg_df = pd.DataFrame(filtered_df.groupby(
    'GEOID')['price_sf'].median()).reset_index()

# Format the price / SF column so it looks nicer
agg_df['price_sf_formatted'] = agg_df['price_sf'].apply(
    lambda x: '${:.0f}'.format(x))

# # Take a look at the data - filtered, aggregated
# st.dataframe(agg_df, use_container_width=True)

# Use the same process as before to get Fulton County's Census tracts
CT_url = "https://services1.arcgis.com/Ug5xGQbHsD8zuZzM/arcgis/rest/services/ACS 2022 Demographic Population GeoSplitJoined/FeatureServer/19/query?where=GEOID%20LIKE%20'13121%25'&outFields=GEOID&outSR=4326&f=json"
CT_url = CT_url.replace(" ", "%20")
CTs_gdf = gpd.read_file(CT_url)

# simplify geometry for more performant web application
CTs_simplified = tp.Topology(CTs_gdf, toposimplify=0.001).to_gdf()

# Merge the grouped sales to the geography so it can be mapped
final_df = gpd.GeoDataFrame(agg_df.merge(CTs_simplified, on='GEOID'))

# define a figure with all pertinent parameters
fig = px.choropleth_mapbox(
    final_df,
    geojson=final_df.geometry,
    locations=final_df.index,
    hover_data=["GEOID", "price_sf_formatted"],
    color="price_sf",
    center={
        "lat": 33.8541,
        "lon": -84.3974},
    mapbox_style=f'carto-{basemap_dictionary[basemap_select]}',
    color_continuous_scale="Blues",
    zoom=8.3,
    height=575,
    opacity=0.7,
)

# Define the fields for the tooltip
fig.update_traces(
    hovertemplate="<b>Census Tract %{customdata[0]}</b><br>%{customdata[1]} per SF",
    marker_line_color='rgba(0, 0, 0, 0)',
    marker_line_width=0
)

# Style the tooltip and configure legend
fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Arial"),
    coloraxis_colorbar=dict(
        title="Median home sale price",
        ticks="outside",
        tickvals=[100, 200, 300, 400],
        tickprefix='$',
        ticksuffix=' / SF'
    ))

# # Call the plotly_chart method to show the choropleth map in the application
# st.plotly_chart(
#     fig,
#     use_container_width=True,
#     config={'displayModeBar': False}
# )
