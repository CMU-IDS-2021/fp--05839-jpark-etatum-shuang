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

def main():
    st.title("Density of Listings!")
    st.write("Hello")
    dataframes = load()
    
    listing = dataframes["listings (1).csv"]
    st.write(listing)
    geo = listing[["id", "latitude", "longitude"]]
    displayMap(geo)
    graph(listing)

@st.cache    
def load():
    dataframes = {}
    files = os.listdir("Data/small")
    for f in files:
        if f.split(".")[-1] == "csv":
            try:
                df = pd.read_csv("data/" + f)
                #print(df)
                #print(df.columns)
                dataframes[f] = df
            except:
                print("file too big: " + f)
    return dataframes
    
    
def displayMap(map):
    
    blur = st.checkbox("Blur")
    large = st.checkbox("Large Points")
    add = 0
    if large:
        add = 6
    if blur:
        b = 15
        rad = 20 + add
    else:
        b = 1
        rad = 4 + add
    st.write("Airbnb Listing density Heat Map")
    hmap = folium.Map(location=[34, -118.5], zoom_start=9)

    hm_wide = HeatMap(map[['latitude','longitude']], radius=5,
        min_opacity=0, blur=1, control_scale = True)

    hmap.add_child(hm_wide)
    folium_static(hmap)

    
def graph(df):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    df = df[['id','neighbourhood']]
    df = df.groupby('neighbourhood').count().reset_index()
    df = df.rename(columns={"id":"Number of Listings"})
    
    columns = st.slider('Columns', 5, 40, 10)
    asc = st.checkbox('Descending')
    df = df.sort_values(by='Number of Listings', ascending = asc).head(columns)
    
    plot = sns.barplot(data=df, x = df['neighbourhood'], y = df['Number of Listings'], palette = sns.color_palette(n_colors=1))
    plt.setp(plot.get_xticklabels(), rotation=90)
    st.pyplot()
    
    
    
main()