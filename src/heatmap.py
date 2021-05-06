import pandas as pd
import streamlit as st
from src.utils import generate_heatmap


def heatmap_chart():
	# headers and stuff
	st.header("Part 3: Heatmap of Airbnb occupancy rate")

	# generate second chart
	st.markdown("Now comes the interesting part, what are the occupancy rate of Airbnb housing? "
				"The following heatmap will tell you about it.")

	st.markdown("The heatmap below shows a obvious trend of drop in occupancy rate. "
				"Especially the comparision between the year 2015/2016 and 2020/2021, heatmap are much more yellow in "
				"previous years and blue in recent years, which could be the outcome of Covid-19.")

	chart1 = generate_heatmap()
	st.plotly_chart(chart1)

	st.header("Analysis")
	st.markdown("The low spectrum indicated close to max occupancy while high referenced vacancy. We were able to see that the occupancy rates average around 0.45 - 0.75. In 2020 - 2021, we saw the occupancy rate was slightly lower than average likely due to macroeconomic drivers (e.g COVID-19), though the impact was minimal. These rates are important to analyze so we can get an understanding of the demand for rental properties, which can indicate high conversion into short term rentals.")

	pass
