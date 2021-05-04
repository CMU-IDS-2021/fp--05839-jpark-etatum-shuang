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

	# generate first chart
	st.markdown("First, we took a look at the time trend of average pricing "
				"data in Airbnb. We use different color to separate years of data."
				"We can actually see that average price are going up year by year despite some "
				"minor outliners in between.")
	chart1 = generate_line_chart_all()
	st.altair_chart(chart1)

	# generate second chart
	st.markdown("Secondly, we made an interactive chart below to let you explore on your own. Select"
				"the years you want to check out and shift-click on the bars to change the transparency of lines."
				"And move your mouse to choose the date & average housing price of that day.")
	years = st.multiselect('what years do you want to check out',
							 [2015, 2016, 2017, 2018, 2019, 2020, 2021],
							 [2015, 2016])
	chart2 = generate_line_chart(years)
	st.altair_chart(chart2)

	pass
