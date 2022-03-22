from fetch_data import fetch_data
from pprint import pprint
url = 'https://restcountries.com/v2/all'
data = fetch_data(url)

""" for country in data[:10]:
	languages = ', '.join(list(map(lambda l:l['name'], country['languages'])))
	print([country['name'], country['population'], country.get('capital'), languages])

print(len(data)) """


# new_lst = [[country['name'], country['population']] for country in data]
new_lst = list(map(lambda c:[c['name'], c['population']], data))
sorted_countries = sorted(new_lst, key= lambda x:x[1], reverse=True)
ten_most_populated_countries = sorted_countries[:10]
pprint(ten_most_populated_countries)