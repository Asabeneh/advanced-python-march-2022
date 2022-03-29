import requests
class FetchData:
	def __init__(self, url):
		self.url = url
		pass
	def fetch_json_data(self):
		response = requests.get(self.url)
		data = response.json()
		return data

	def fetch_text_data(self):
		response = requests.get(self.url)
		data = response.text
		return data