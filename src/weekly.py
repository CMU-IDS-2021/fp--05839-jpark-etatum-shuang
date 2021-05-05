import pandas as pd
import streamlit as st
from src.utils import generate_violin_chart


def violin_chart():
	# headers and stuff
	st.header("Part 2: Weekly price of Airbnb housing")


	# generate second chart
	st.markdown("It is important to evaluate the cost of weekly stays as it gives us insight into longer term stays in the area. Longer term stays ")
	st.markdown("The second part of our project is to explore trends between different days of week. We assume that "
				"work days housing prices are lower than weekends. We made a violin chart to prove our point. "
				"Same as usual, select the years you want to visualize and prove it by yourself.")
	year = st.selectbox('choose the years you want to visualize',
						[2015, 2016, 2017, 2018, 2019, 2020, 2021],
						0)
	chart1 = generate_violin_chart(year)
	st.plotly_chart(chart1)

	pass
