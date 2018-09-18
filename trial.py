import pdb; pdb.set_trace()
import requests
import bleach
import yaml
from bs4 import BeautifulSoup

page = requests.get('https://codequs.com/')
soup = BeautifulSoup(page.text, 'html.parser')


block_list = soup.find_all('div', {'class' : 'col-xs-12 col-lg-4 col-md-6 col-sm-12'})
print(block_list)

with open("trial.txt", "w") as file:
	for block in block_list:
		
		#find all path link go to detail tutorial start with <a>
		links_text = block.find('a')
		print(links_text)

		#find all title tutorial start with <h2 class>
		title_list_2 = block.find('h4', {'class': 'card-title'})

		#create new url for each tutorial transplate with main url
		links = 'https://codequs.com/'+ links_text.get('href')

		print("title:" ,title_list_2)
		print("url:", links)

