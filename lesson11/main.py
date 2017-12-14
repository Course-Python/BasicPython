import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://docs.python.org/3/'

response = requests.get(BASE_URL)

# print(response.status_code)
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

links = []
for table in soup.find_all('table'):
	links += table.find_all('a')

with open('categories.txt', 'w') as f_out:
	for link in links:
		text = f'{link.text}: {BASE_URL}{link.get("href")}'
		f_out.write(text + '\n')
