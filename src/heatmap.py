import pandas as pd
import streamlit as st
from src.utils import generate_heatmap


def heatmap_chart():
	# headers and stuff
	st.header("Part 3: Heatmap of Airbnb occupancy rate")
	st.markdown("First, we took a state and national view to the data to understand the breakdown segmentations of data in Yelp. Select from the slider on the left to switch between views.")

	# generate second chart
	st.markdown("")
	chart1 = generate_heatmap()
	st.plotly_chart(chart1)

	pass
