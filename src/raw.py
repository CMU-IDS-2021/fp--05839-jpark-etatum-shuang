import pandas as pd
import streamlit as st
from src.utils import generate_raw_chart

def raw_data():
	# breaking down the data
	st.header("Part 0: Understanding the Airbnb Dataset")
	st.markdown("There are multiple unique columns in the Business Yelp dataset "
				"including business id, name, categories, reviews, address and latitude / longitude that we used for the analysis.")
	st.markdown("We began digging into the types of data available to understand "
				"how users may identify the distribution of the types of food across different regions and domains.")

	# generate dataframe from raw data
	charts = generate_raw_chart()

	st.markdown("First we'll take a look at the calendar dataset")
	st.write(charts[0])

	st.markdown("Second we'll take a look at the calendar dataset")
	st.write(charts[1])

	st.markdown("Third we'll take a look at the calendar dataset")
	st.write(charts[2])

	st.markdown("Finally we'll take a look at the calendar dataset")
	st.write(charts[3])
