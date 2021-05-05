import streamlit as st
import pandas as pd

#chart by neighborhood
@st.cache
def pull_data():
	return pd.read_csv("http://data.insideairbnb.com/united-states/ca/los-angeles/2021-04-07/visualisations/listings.csv")

def table_chart():
	df = pull_data()
	st.header("Part 6: Most Expensive Price by Property Areas")
	st.subheader("Raw Data")
	st.dataframe(df.head())
	st.markdown("Following are the top five most expensive properties.")
	st.write(df.query("price>=1000").sort_values("price", ascending=False).head())
	st.subheader("Shockingly, Airbnb property prices in Los Angeles can be over $21,000.")
	st.subheader("Map Visualization")
	st.markdown("Based on the most recent Insider Airbnb data, the map showcases Airbnbs priced at over $1000 and the top percentiles of housing prices.")
	st.map(df.query("price>=1000")[["latitude", "longitude"]].dropna(how="any"))
	st.subheader("Our data found that the most expensive areas of Los Angeles are Santa Monica, Venice and Beverly Hills.")

