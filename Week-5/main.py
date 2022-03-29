from fetch_data import FetchData

url = 'https://api.thecatapi.com/v1/breeds'

cat_data = FetchData(url).fetch_json_data()
# print(cat_data)
url = 'https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'
shakespeare_note = FetchData(url).fetch_text_data()
print(shakespeare_note)

import webbrowser 

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for link in url_lists:
	webbrowser.open_new(link)