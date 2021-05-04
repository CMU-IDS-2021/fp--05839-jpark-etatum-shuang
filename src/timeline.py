import streamlit as st
from src.utils import generate_line_chart_all, generate_line_chart

dates = ["2021-02-07",
		 "2020-10-09",
		 "2020-08-20", "2020-05-08", "2020-02-13",
		 "2019-11-19", "2019-08-08", "2019-05-05", "2019-02-03",
		 "2018-11-04", "2018-08-07", "2018-05-09", "2018-03-07",
		 "2017-05-02", "2017-03-02",
		 "2016-08-03", "2016-05-02", "2016-01-02",
		 "2015-11-06", "2015-07-25", "2015-05-24"
		 ]


def line_chart():
	# headers and stuff
	st.header("Part 1: Average price of Airbnb housing")
	st.markdown("First, we took a state and national view to the data to understand the breakdown"
				"segmentations of data in Yelp. Select from the slider on the left to switch between views.")

	# generate first chart
	st.markdown("")
	chart1 = generate_line_chart_all()
	st.altair_chart(chart1)

	# generate second chart
	st.markdown("")
	years = st.multiselect('What are your favorite colors',
							 [2015, 2016, 2017, 2018, 2019, 2020, 2021],
							 [2015, 2016])
	chart2 = generate_line_chart(years)
	st.altair_chart(chart2)

	pass
