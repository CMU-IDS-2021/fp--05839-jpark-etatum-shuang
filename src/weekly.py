import pandas as pd
import streamlit as st
from src.utils import generate_violin_chart


def violin_chart():
	# headers and stuff
	st.header("Part 2: Weekly price of Airbnb housing")
	st.markdown("First, we took a state and national view to the data to understand the breakdown segmentations of data in Yelp. Select from the slider on the left to switch between views.")

	# generate second chart
	st.markdown("")
	year = st.selectbox('choose the years you want to visualize',
						[2015, 2016, 2017, 2018, 2019, 2020, 2021],
						0)
	chart1 = generate_violin_chart(year)
	st.plotly_chart(chart1)

	pass
