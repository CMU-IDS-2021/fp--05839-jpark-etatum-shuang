import pandas as pd
import streamlit as st
from src.utils import generate_raw_chart

def raw_data():
	# breaking down the data
	st.header("Part 0: Understanding the Airbnb Dataset")
	st.markdown("There are multiple unique columns in the Airbnb dataset "
				"including date, price and check-in data that we used for the analysis.")

	# generate dataframe from raw data
	charts = generate_raw_chart()

	st.markdown("First we'll take a look at the calendar dataframe")
	st.write(charts[0])

	st.markdown("Second we'll take a look at the listing dataframe")
	st.write(charts[1])

	st.markdown("Third we'll take a look at the review dataframe")
	st.write(charts[2])

	st.markdown("Finally we'll take a look at the cut and filtered words generated from the review dataframe."
				"We'll later use the those words to generate a word cloud")
	st.write(charts[3])
