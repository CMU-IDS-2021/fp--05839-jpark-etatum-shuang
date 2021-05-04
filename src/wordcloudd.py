import pandas as pd
import streamlit as st
from src.utils import generate_word_cloud, generate_bar_chart


def wordcloud_chart():
	# headers and stuff
	st.header("Part 4: Word cloud of Airbnb review")

	# generate second chart
	st.markdown("Last but not least, word cloud! We made use of the review database and use jieba library to "
				"extract words out of reviews, then we filtered both stopwords and nounces to make sure the word cloud"
				"is meaningful. Now check out the word clouds of review and see if there's any changes between the years.")
	year = st.selectbox('choose the years you want to visualize',
						[2015, 2016, 2017, 2018, 2019, 2020, 2021],
						0)
	generate_word_cloud(year)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()

	# more positive vs negative
	st.markdown("Now let's see the positive review rate among the years, you can see that despite the poor positive rate"
				"in 2011, positive rate drops steadily each year which indicates a drop of customer satisfaction.")
	chart = generate_bar_chart()
	st.altair_chart(chart)

