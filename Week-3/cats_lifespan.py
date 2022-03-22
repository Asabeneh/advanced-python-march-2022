from fetch_data import fetch_data
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_data(url)

life_spans = []
for cat in data:
	min_age = int(cat['life_span'].split(' - ')[0])
	max_age = int(cat['life_span'].split(' - ')[1])
	age = (min_age  + max_age) / 2
	life_spans.append(age)


average_life_span = (sum(life_spans) / len(life_spans))
print(round(average_life_span, 2))
print(sorted(life_spans, reverse=True))
