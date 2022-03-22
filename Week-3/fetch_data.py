def fetch_data(url):
	import requests
	response = requests.get(url)
	data = response.json()
	return data
