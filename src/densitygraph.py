import os
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
import seaborn as sns
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import matplotlib.pylab as plt 
from src.utils import get_data_cached
import altair as alt

def main():
    st.title("Density of Airbnb Listings")
    listing = load()
    geo = listing[["id", "latitude", "longitude"]]
    displayMap(geo)
    graph(listing)
    check = st.checkbox('Show Neighbourhoods Over Time', value=True)
    if check:
        time_analysis()

@st.cache    
def load():
    listing_pd = pd.read_csv("./Data/listings/listingsapr2021.csv")
    return listing_pd
    
    
def displayMap(map):

    st.write("Airbnb Listing density Heat Map")
    hmap = folium.Map(location=[34, -118.5], zoom_start=9)

    hm_wide = HeatMap(map[['latitude','longitude']], radius=5,
        min_opacity=0, blur=1, control_scale = True)

    hmap.add_child(hm_wide)
    folium_static(hmap)

    
def graph(df):
    st.write("Number of listings per LA Neighbourhood")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    df = df[['id','neighbourhood']]
    df = df.groupby('neighbourhood').count().reset_index()
    df = df.rename(columns={"id":"Number of Listings"})
    df = df.rename(columns={"neighbourhood":"Neighbourhood"})
    
    columns = st.slider('Number of Neighbourhoods to Display', 5, 40, 10)
    asc = st.checkbox('Show Ascending')
    df = df.sort_values(by='Number of Listings', ascending = asc).head(columns)
    
    plot = sns.barplot(data=df, x = df['Neighbourhood'], y = df['Number of Listings'], palette = sns.color_palette(n_colors=1))
    plt.setp(plot.get_xticklabels(), rotation=90)
    st.pyplot()
   
def time_analysis():
    listing_apr_2021 = pd.read_csv("./Data/listings_time/listings2021.csv")
    listing_mar_2021 = pd.read_csv("./Data/listings_time/listings20212.csv")
    listing_feb_2021 = pd.read_csv("./Data/listings_time/listings2020.csv")
    listing_jan_2021 = pd.read_csv("./Data/listings_time/listings20202.csv")
    listing_dec_2020 = pd.read_csv("./Data/listings_time/listings2019.csv")
    listing_nov_2020 = pd.read_csv("./Data/listings_time/listings20192.csv")
    listing_oct_2020 = pd.read_csv("./Data/listings_time/listings2018.csv")
    listing_sep_2020 = pd.read_csv("./Data/listings_time/listings20182.csv")
    listing_aug_2020 = pd.read_csv("./Data/listings_time/listings2017.csv")

    
    df_list = [listing_apr_2021,listing_mar_2021,listing_feb_2021,listing_jan_2021,
        listing_dec_2020,listing_nov_2020,listing_oct_2020,listing_sep_2020,
        listing_aug_2020] 
    time_list = ["JUN2021","JAN2021","JUN2020","JAN2020","JUN2019","JAN2019","JUN2018","JAN2018","JUN2017"]
    time_list = [datetime.strptime(x, '%b%Y') for x in time_list]    
    list_all_neighbourhoods = df_list[0].groupby('neighbourhood').count().reset_index()['neighbourhood'].tolist()
    
    neighbourhoods = st.multiselect("Select Nieghbourhoods To Display",list_all_neighbourhoods, ["Hollywood", "Venice", "Long Beach"])
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(df_list)):
        df = df_list[i]
        df = df.groupby('neighbourhood').count().reset_index()
        df = df[df["neighbourhood"].isin(neighbourhoods)]
        for j in range(len(neighbourhoods)):
            l1.insert(0,time_list[i])
            try:
                l2.insert(0,df.iloc[j]['id'])
            except:
                l2.insert(0,0)
            l3.insert(0,neighbourhoods[j])
        
    data = pd.DataFrame(data = {'time' : l1, 'count' : l2, 'neighbourhood' : l3})
    chart = alt.Chart(data).mark_line().encode(
    x=alt.X('time:T', axis = alt.Axis(format=("%b%Y"))),
    y=alt.Y('count:Q', axis = alt.Axis(title="Number of Listings")),
    color=alt.Color("neighbourhood:N")
    ).properties(title="Change in Listings Over Time")
    st.altair_chart(chart, use_container_width=True)
        
    
    
def density_chart():
    main()
    
