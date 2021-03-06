import streamlit as st
import pandas as pd
from typing import Dict, Callable
from src.raw import raw_data
from src.timeline import line_chart
from src.weekly import violin_chart
from src.heatmap import heatmap_chart
from src.wordcloudd import wordcloud_chart
from src.densitygraph import density_chart
from src.expensive import table_chart

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

def conclusion():
	st.header("Conclusion")
	st.subheader("Findings:")
	st.markdown("The visualizations helped us identify core insights. First, we were able to see similar trends around the price of Airbnbs in the locations where we saw trends of gentrification across Los Angeles. Secondly, we saw that these same areas has the highest prices within the same areas. The price of Airbnb in Hollywood and Venice have skyrocketed along with the number of Airbnbs within a population area. Finally, we found that there were a significant cluster of long term stays in the region which drives revenue to a population with significant wealth and power.")

	st.markdown("We did secondary research around what areas of Los Angeles were impacted by gentrification to compare to our results and insights. Here are L.A.’s top 10 most gentrified communities based on the Los Angeles Time below: Downtown, Venice, Hollywood, Silver Lake and Echo Park.")
	st.image('img/image2.png', use_column_width=True)

	st.subheader("Future Implications:")
	st.markdown("In the future, our team would love to take our visualization and exploration another step forward. We would like to leverage more machine learning based models. We would like to use NLP models on the Airbnb reviews. More thorough models could provide greater fidelity in what is desired by renters. Other techniques such as sentiment analysis could help determine what factors lead to high renter satisfaction. We would also like to leverage machine learning to potentially predict future trends. ")

	st.markdown("We would also be interested in incorporating other methods of measuring gentrification and adding it to our own visualizations. While we have referenced other sources to verify our findings, we would like to incorporate other common ways of measuring gentrification using sources such as the census. This could provide a more complex picture of gentrification, but we could also see how rental data relates to other indicators in both time and intensity.")

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
	    "Location Density",
		"Most Expensive Housing",
		"Conclusion"
    ],
)
page_function_mapping: Dict[str, Callable[[pd.DataFrame], None]] = {
	"Raw data understanding": raw_data,
	"Time trend": line_chart,
	"Weekly trend": violin_chart,
	"Heat map": heatmap_chart,
    "Word cloud": wordcloud_chart,
	"Location Density" : density_chart,
	"Most Expensive Housing": table_chart,
	"Conclusion": conclusion

}
page_function_mapping[page]()

# other mark downs
st.sidebar.markdown(
        """
    **Please note**:

    Many of the plots are interactive, you can zoom with scrolling and hover on data points for additional information.
    """
)

