import pandas as pd
import streamlit as st
from src.utils import generate_heatmap


def heatmap_chart():
	# headers and stuff
	st.header("Part 3: Heatmap of Airbnb occupancy rate")

	# generate second chart
	st.markdown("Now comes the interesting part, what are the occupancy rate of Airbnb housing? "
				"The following heatmap will tell you about it.")
	chart1 = generate_heatmap()
	st.plotly_chart(chart1)

	pass
