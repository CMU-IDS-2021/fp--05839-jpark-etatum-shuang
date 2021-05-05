import streamlit as st
import pandas as pd
from typing import Dict, Callable
from src.raw import raw_data
from src.timeline import line_chart
from src.weekly import violin_chart
from src.heatmap import heatmap_chart
from src.wordcloudd import wordcloud_chart
from src.densitygraph import density_chart

# Title
st.title("Airbnb Data Analysis 📊")
st.markdown("			By Shicheng Huang, Jennifer Park, Eric Tatum")
st.markdown("			In this project, we will take you through an narrative tour with "
			"the Inside Airbnb dataset. We will then tie this data to larger Los Angeles dentrification trends in Los Angeles. We will make use of different attribute of this dataset "
			"and tell a compelling story with the data we have available.")

# Introduction
st.header("Project Purpose")
st.markdown("Our project aims to examine the impact of the growth of Airbnb in Los Angeles and tying the data visualization to gentrification within the city. Our team will be using data from Inside Airbnb to visualize listing, pricing and property attributes. ")

st.header("Project Hypothesis")
st.markdown("We hypothesize that short term and long term rental services driven by Airbnb drive the displacement of communities by introducing a new revenue flow into traditionally low income housing markets.")


st.image('img/image1.png', use_column_width=True)


st.header("Project Background")
st.markdown("Gentrification is the process by which neighborhoods are transformed such that neighborhoods that were once housed and catered to marginalized populations are impacted by an influx of middle and upper class residents which shifts the power dynamic and resource options available in the neighborhood. ")
st.markdown("Airbnb has changed the way guests travel with the platform by directly embedding middle to upper class consumers within the community. This subsequently has significant impacts on the community where consumer temporarily reside. The popularity of Airbnb has driven investment property moguls to purchase low income housing that is necessary for the livelihood of low income households. ")


st. markdown("Although Airbnb emphasizes empowering local home owners to supplement their income, Airbnb disproportionately impacts consumers in low income areas. Additionally, residents shape resources that is desirable in these areas. ")

# Page choice
st.sidebar.title("Page")
page = st.sidebar.selectbox(
    label="Page",
    options=[
		"Raw data understanding",
		"Time trend",
		"Weekly trend",
		"Heat map",
        	"Word cloud",
	    	"Location Density"
    ],
)
page_function_mapping: Dict[str, Callable[[pd.DataFrame], None]] = {
	"Raw data understanding": raw_data,
	"Time trend": line_chart,
	"Weekly trend": violin_chart,
	"Heat map": heatmap_chart,
    	"Word cloud": wordcloud_chart,
	"Location Density" : density_chart
}
page_function_mapping[page]()

# other mark downs
st.sidebar.markdown(
        """
    **Please note**:

    Many of the plots are interactive, you can zoom with scrolling and hover on data points for additional information.
    """
)
