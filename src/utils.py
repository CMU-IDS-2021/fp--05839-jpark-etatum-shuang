import pandas as pd
import altair as alt
import streamlit as st
import plotly.graph_objects as go
import nltk
nltk.download('stopwords')
import multidict as multidict


import pandas as pd
dates = ["2021-02-07",
		 "2020-10-09",
		 "2020-08-20", "2020-05-08", "2020-02-13",
		 "2019-11-19", "2019-08-08", "2019-05-05", "2019-02-03",
		 "2018-11-04", "2018-08-07", "2018-05-09", "2018-03-07",
		 "2017-05-02", "2017-03-02",
		 "2016-08-03", "2016-05-02", "2016-01-02",
		 "2015-11-06", "2015-07-25", "2015-05-24"
		 ]

def apply_date(date):
	#     splited = date.split("/")
	return date + " 00:00:00"

def apply_price(price):
	try:
		price = price.replace("$", "")
		price = price.replace(",", "")
		return float(price)
	except:
		return float(price)

@st.cache
def get_data():
	# get data
	calendar_pd = None
	for d in dates:
		file_path = f"/Users/huangbenson/Work/cmu/05-839/assignments/a3/data/{d}_calendar.csv"
		if calendar_pd is None:
			calendar_pd = pd.read_csv(file_path)
			calendar_pd = calendar_pd.sample(100)
			calendar_pd.date = calendar_pd.date.apply(apply_date)
			calendar_pd.price = calendar_pd.price.apply(apply_price)
		else:
			append_pd = pd.read_csv(file_path)
			append_pd = append_pd.sample(100)
			append_pd.date = append_pd.date.apply(apply_date)
			append_pd.price = append_pd.price.apply(apply_price)
			calendar_pd = pd.concat([calendar_pd, append_pd], axis=0)

	listing_pd = None
	for d in dates:
		file_path = f"/Users/huangbenson/Work/cmu/05-839/assignments/a3/data/{d}_listings.csv"
		if listing_pd is None:
			listing_pd = pd.read_csv(file_path)
			listing_pd = listing_pd.sample(100)
			listing_pd["date"] = d + " 00:00:00"
			listing_pd.price = listing_pd.price.apply(apply_price)
		else:
			append_pd = pd.read_csv(file_path)
			append_pd = append_pd.sample(100)
			listing_pd["date"] = d + " 00:00:00"
			append_pd.price = append_pd.price.apply(apply_price)
			listing_pd = pd.concat([listing_pd, append_pd], axis=0)

	review_pd = None
	for d in dates:
		file_path = f"/Users/huangbenson/Work/cmu/05-839/assignments/a3/data/{d}_reviews.csv"
		if review_pd is None:
			review_pd = pd.read_csv(file_path)
			review_pd = review_pd.sample(100)
		else:
			append_pd = pd.read_csv(file_path)
			append_pd = append_pd.sample(100)
			review_pd = pd.concat([review_pd, append_pd], axis=0)

	# add year & weekly chart & month
	def add_year(date):
		return int(date[0: 4])

	def add_month(date):
		return int(date[5: 7])

	calendar_pd["year"] = calendar_pd.date.apply(add_year)
	calendar_pd["month"] = calendar_pd.date.apply(add_month)

	# add partial date
	def add_partial_date(date):
		return date[5:10]

	def add_clean_date(date):
		return date[0:10]

	calendar_pd["partial_date"] = calendar_pd.date.apply(add_partial_date)
	calendar_pd["clean_date"] = calendar_pd.date.apply(add_clean_date)

	# add week of day
	import datetime
	week_of_day_mapping = {
		0: "Mon",
		1: "Tue",
		2: "Wed",
		3: "Thr",
		4: "Fri",
		5: "Sat",
		6: "Sun",
	}

	def add_week_ofday(date):
		date = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]))
		return week_of_day_mapping[date.weekday()]

	calendar_pd["weekofday"] = calendar_pd.date.apply(add_week_ofday)

	# word cloud
	import paddlehub as hub
	senta = hub.Module(name="senta_lstm")
	def apply_positive(row):
		if type(row) != str:
			return "positive"
		else:
			return senta.sentiment_classify(data={"text": [row]})[0]["sentiment_key"]

	review_pd["positive"] = review_pd.comments.apply(apply_positive)

	# jieba
	import jieba
	def apply_jieba(row):
		a = jieba.cut(row)
		try:
			return list(jieba.cut(row.lower()))
		except:
			return []

	review_pd["jieba"] = review_pd.comments.apply(apply_jieba)

	# add year
	def add_year(date):
		return int(date[0: 4])

	review_pd["year"] = review_pd.date.apply(add_year)

	# jieba
	from collections import defaultdict
	review_map = {
		2010:defaultdict(int),
		2011:defaultdict(int),
		2012:defaultdict(int),
		2013:defaultdict(int),
		2014:defaultdict(int),
		2015:defaultdict(int),
		2016:defaultdict(int),
		2017:defaultdict(int),
		2018:defaultdict(int),
		2019:defaultdict(int),
		2020:defaultdict(int),
		2021:defaultdict(int)
	}

	pos_map = {

	}

	for index, row in review_pd.iterrows():
		for word in row["jieba"]:
			review_map[row["year"]][word] += 1
			pos_map[word] = row["positive"]

	from nltk.corpus import stopwords
	import nltk, re
	import multidict as multidict

	review_map_new = {
		2010:multidict.MultiDict(),
		2011:multidict.MultiDict(),
		2012:multidict.MultiDict(),
		2013:multidict.MultiDict(),
		2014:multidict.MultiDict(),
		2015:multidict.MultiDict(),
		2016:multidict.MultiDict(),
		2017:multidict.MultiDict(),
		2018:multidict.MultiDict(),
		2019:multidict.MultiDict(),
		2020:multidict.MultiDict(),
		2021:multidict.MultiDict()
	}
	stop = stopwords.words('english')

	for year, dic in review_map.items():
		for k, v in dic.items():
			if k.lower() not in stop and bool(re.search('[a-z]', k)):
				review_map_new[year].add(k, v)

	return calendar_pd, listing_pd, review_pd, review_map_new


@st.cache
def get_data_cached():
	import pickle
	calendar_pd = pd.read_csv("./Data/processed/calendar.csv")
	listing_pd = pd.read_csv("./Data/processed/listing.csv")
	review_pd = pd.read_csv("./Data/processed/review.csv")
	with open('./Data/processed/review_map.pkl', 'rb') as f:
		review_map_new = pickle.load(f)

	return calendar_pd, listing_pd, review_pd, review_map_new


calendar_pd, listing_pd, review_pd, review_map_new = get_data_cached()


def generate_line_chart_all(
	width: int = 700,
	height: int = 500,
) -> alt.Chart:
	# select a point for which to provide details-on-demand
	label = alt.selection_single(
		fields=['year'],  # limit selection to x-axis value
		empty='none'      # empty selection includes no data points
	)

	# define our base line chart of stock prices
	base = alt.Chart(calendar_pd).mark_line().encode(
		alt.X('date:T'),
		alt.Y('price:Q'),
		alt.Color('year:N')
	)

	final_chart = alt.layer(
		base,   # base line chart

		# add a rule mark to serve as a guide line
		alt.Chart().mark_rule(color='#aaa').encode(
			x='date:T'
		).transform_filter(label),

		# add circle marks for selected time points, hide unselected points
		base.mark_circle().encode(
			opacity=alt.condition(label, alt.value(1), alt.value(0))
		).add_selection(label),

		# add white stroked text to provide a legible background for labels
		base.mark_text(align='left', dx=5, dy=-5, stroke='white', strokeWidth=2).encode(
			text='price:Q'
		).transform_filter(label),

		# add text labels for stock prices
		base.mark_text(align='left', dx=5, dy=-5).encode(
			text='price:Q'
		).transform_filter(label),

	).configure_view(strokeWidth=0).properties(
		width=width,
		height=height
	).interactive()

	return final_chart


def generate_line_chart(
	years: list,
	width: int = 700,
	height: int = 500,
) -> alt.Chart:
	# filter data
	calendar_pd_filtered = calendar_pd.drop_duplicates(subset=['date'], keep='first')
	calendar_pd_filtered = calendar_pd_filtered[calendar_pd_filtered.price < 5000]
	calendar_pd_filtered = calendar_pd_filtered[calendar_pd_filtered.price.notna()]

	# select a point for which to provide details-on-demand
	click = alt.selection_multi(
		fields=['year'], # limit selection to x-axis value
		empty='none',     # empty selection includes no data points
		init=[{"year": years[0]}]
	)

	# select a point for which to provide details-on-demand
	hover = alt.selection_single(
		encodings=['x'], # limit selection to x-axis value
		on='mouseover',  # select on mouseover events
		nearest=True,    # select data point nearest the cursor
		empty='none'     # empty selection includes no data points
	)

	# legend
	legend = alt.Chart(calendar_pd_filtered).mark_point().encode(
		y=alt.Y('year:N', axis=alt.Axis(orient='right')),
		color=alt.condition(click,
							alt.Color('year:N', legend=None),
							alt.value('lightgray'))
	).add_selection(
		click
	).transform_filter(
		alt.FieldOneOfPredicate(field='year', oneOf=years)
	)

	# define our base line chart of stock prices
	base = alt.Chart(calendar_pd_filtered).mark_line().encode(
		x=alt.X('partial_date:T'),
		y=alt.Y('price:Q'),
		color=alt.Color('year:N', legend=None)
	).transform_filter(
		alt.FieldOneOfPredicate(field='year', oneOf=years)
	)

	final_chart = alt.layer(
		base.encode(opacity=alt.condition(click, alt.value(1), alt.value(0.1))), # base line chart

		# add a rule mark to serve as a guide line
		alt.Chart(calendar_pd_filtered).mark_rule(color='#aaa').encode(
			x='partial_date:T'
		).transform_filter(hover),

		# add circle marks for selected time points, hide unselected points
		base.mark_circle().encode(
			opacity=alt.condition(hover, alt.value(1), alt.value(0))
		).add_selection(hover).transform_filter(click),

		# add white stroked text to provide a legible background for labels
		base.mark_text(align='left', dx=5, dy=-5, stroke='white', strokeWidth=2).encode(
			text=alt.Text('label:N')
		).transform_filter(hover).transform_filter(click).transform_calculate(label=f'"price:$" + datum.price + " date:" + datum.clean_date'),

		# add text labels for stock prices
		base.mark_text(align='left', dx=5, dy=-5).encode(
			text='label:N'
		).transform_filter(hover).transform_filter(click).transform_calculate(label=f'"price:$" + datum.price + " date:" + datum.clean_date'),

	).properties(
		width=width,
		height=height,
		title="price over time"
	).interactive() | legend

	return final_chart


def generate_violin_chart(
	year: int,
):
	# generate years
	calendar_pd_filtered = calendar_pd[calendar_pd.price < 1000]
	calendar_pd_filtered_lst = []
	for d in ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]:
		calendar_pd_filtered_lst.append(calendar_pd_filtered[calendar_pd_filtered.date.map(lambda x: x.startswith(d))])

	# generate graph
	choose = year
	df = calendar_pd_filtered_lst[choose - 2015]
	days = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
	fig = go.Figure()
	for day in days:
		fig.add_trace(go.Violin(x=df['weekofday'][df['weekofday'] == day],
								y=df['price'][df['weekofday'] == day],
								name=day,
								box_visible=True,
								meanline_visible=True))
	return fig


def generate_heatmap(
):
	# group by
	def available_rate(row):
		count_all = row["available"].count()
		count_t = row["available"][row["available"] == "t"].count()
		return count_t/count_all * 1.0

	count = calendar_pd.groupby(["year", "month"]).apply(available_rate)
	count = pd.DataFrame(count)
	count.reset_index(inplace=True)

	# change month
	mapping_month = {
		1: "Jan",
		2: "Feb",
		3: "Mar",
		4: "Apr",
		5: "May",
		6: "Jun",
		7: "Jul",
		8: "Aug",
		9: "Sep",
		10: "Oct",
		11: "Nov",
		12: "Dec"
	}
	def change_of_month(month):
		return mapping_month[month]

	count["month_str"] = count.month.apply(change_of_month)
	count = count[count.year != 2022]

	# add up
	count.loc[0] = [2015, 5, 0.8, "May"]
	count.index = count.index + 1  # shifting index
	count.sort_index(inplace=True)
	count.loc[0] = [2015, 4, 0.77, "Apr"]
	count.index = count.index + 1  # shifting index
	count.sort_index(inplace=True)
	count.loc[0] = [2015, 3, 0.93, "Mar"]
	count.index = count.index + 1  # shifting index
	count.sort_index(inplace=True)
	count.loc[-1] = [2015, 2, 0.78, "Feb"]
	count.index = count.index + 1  # shifting index
	count.sort_index(inplace=True)
	count.loc[-1] = [2015, 1, 0.87, "Jan"]
	count.index = count.index + 1  # shifting index
	count.sort_index(inplace=True)

	count = count.sort_values("month", kind='mergesort')

	# graph
	fig = go.Figure(data=go.Heatmap(
		z=count[0],
		x=count["month_str"],
		y=count["year"],
		colorscale='Viridis'))

	fig.update_layout(
		title='Monthly occupancy rate',
		xaxis_nticks=36)

	return fig


def generate_word_cloud(
	year: int,
):
	# word cloud
	from wordcloud import WordCloud
	import matplotlib.pyplot as plt

	wc = WordCloud(background_color="white", max_words=1000)
	wc.generate_from_frequencies(review_map_new[2015])

	plt.imshow(wc, interpolation="bilinear")
	plt.axis("off")
	plt.show()


def generate_raw_chart(

):
	return calendar_pd.head(), listing_pd.head(), review_pd.head(), review_map_new[2015]


def generate_bar_chart(

):
	for i in ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]:
		tr = review_pd[review_pd.date.map(lambda x: x.startswith(i))]
		print( tr[tr["positive"] == "positive"].count() / tr.count())
	d = {'year': ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
		 'positive rate': [1, 0.875, 1, 0.985, 0.946, 0.947, 0.943, 0.911, 0.909, 0.91,  0.93, 0.89]}

	pdd = pd.DataFrame(data=d)
	chart = alt.Chart(pdd).mark_bar(
		color='lightblue',
		opacity=0.8
	).encode(
		x=alt.X('year:N'),
		y=alt.Y('positive rate:Q', scale=alt.Scale(domain=[0.7, 1])),
	).properties(
		width=700,
		height=400,
		title="positive review rate "
	).interactive()
	return chart
