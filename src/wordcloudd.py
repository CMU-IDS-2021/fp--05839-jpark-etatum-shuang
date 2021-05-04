import pandas as pd
import streamlit as st
from src.utils import generate_word_cloud


def wordcloud_chart():
	# headers and stuff
	st.header("Part 4: Word cloud of Airbnb review")
	st.markdown("First, we took a state and national view to the data to understand the breakdown segmentations of data in Yelp. Select from the slider on the left to switch between views.")

	# generate second chart
	st.markdown("")
	year = st.selectbox('choose the years you want to visualize',
						[2015, 2016, 2017, 2018, 2019, 2020, 2021],
						0)
	generate_word_cloud(year)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()
	pass
