import requests
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
data = response.json()


weights =[(int(cat['weight']['metric'].split(' - ')[0]) + int(cat['weight']['metric'].split(' - ')[1]))/ 2 for cat in data]
print(weights)

average_weight = round(sum(weights) / len(weights), 2)
print(average_weight)

# loops, Functions, list, list comprehension, fetching data