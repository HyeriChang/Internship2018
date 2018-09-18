import requests			
import csv
from bs4 import BeautifulSoup

headers = {
	'User-Agent' : 'Your Name, example.com',
	'From': 'email@example.com'
}

url = 'https://example.com'

page = requests.get(url, headers = headers)


#tao file csv và viết nd vào
f = csv.writer(open('artist.csv', 'w'))
f.writerow(['Name', 'Link'])

#khoi tao dsach de giu cac trang
pages = []

#muôn thay thế nd mà thêm một thứ j đó vào thẻ dùng append()
for i in range(1, 5):
	url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
	pages.append(url)

for item in pages:
	page = requests.get(item)
	soup = BeautifulSoup(page.text, 'html.parser')

	#loai bo hoan toan tat ca nd ra khoi cay dung phuong thuc decompose()
	last_links = soup.find(class_='AlphaNav')
	last_links.decompose()

	artist_name_list = soup.find(class_='BodyText')
	artist_name_list_items = artist_name_list.find_all('a')


	for artist_name in artist_name_list_items:
		names = artist_name.contents[0]
		links = 'https://web.archive.org'+ artist_name.get('href')

		f.writerow([names, links])

