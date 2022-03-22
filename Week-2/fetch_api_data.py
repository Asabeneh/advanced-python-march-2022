import requests
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
data = response.json()
cat_weights = []
for cat in data:
	weight = cat['weight']['metric'].split(' - ')
	min_weight = int(weight[0])
	max_weigth = int( weight[1])
	average_weight = (min_weight + max_weigth) / 2
	cat_weights.append(average_weight)

print(round(sum(cat_weights) / len(cat_weights), 2))


