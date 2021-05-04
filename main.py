import streamlit as st
import pandas as pd
from typing import Dict, Callable
from src.raw import raw_data
from src.timeline import line_chart
from src.weekly import violin_chart
from src.heatmap import heatmap_chart
from src.wordcloudd import wordcloud_chart

# Title
st.title("Airbnb Data Analysis 📊")
st.markdown("			By Shicheng Huang, Jennifer Park, Eric Tatum")
st.markdown("			In this project, we will take you through an exploitative tour with"
			"the Airbnb dataset. We will make use of different attribute of this dataset "
			"and tell a compelling story with the data we have :D ")

# Page choice
st.sidebar.title("Page")
page = st.sidebar.selectbox(
    label="Page",
    options=[
		"Time trend",
		"Weekly trend",
		"Heat map",
        "Word cloud",
		"Raw data understanding"
    ],
)
page_function_mapping: Dict[str, Callable[[pd.DataFrame], None]] = {
	"Time trend": line_chart,
	"Weekly trend": violin_chart,
	"Heat map": heatmap_chart,
    "Word cloud": wordcloud_chart,
	"Raw data understanding": raw_data
}
page_function_mapping[page]()

# other mark downs
st.sidebar.markdown(
        """
    **Please note**:

    Many of the plots are interactive, you can zoom with scrolling and hover on data points for additional information.
    """
)
