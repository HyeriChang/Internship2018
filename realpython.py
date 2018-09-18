import requests			
import csv
from bs4 import BeautifulSoup
from lxml import html


page = requests.get('https://realpython.com/python-lists-tuples/')
soup = BeautifulSoup(page.text, 'html.parser')

title =soup.find('h1')


author_name_list = soup.find_all('span', {'class' : 'text-muted'})

author_name_list_items = author_name_list[0].find_all('a')

# Comments not have in view-souurce
#comments_list = tree.xpath('//span[@class="disqus-comment-count text-muted"]/text()')
#comments_list = soup.find_all('span', {'class' : 'disqus-comment-count text-muted'})

for tag in author_name_list[0].find_all('a', {'class' : 'badge'}):
	print(tag.text)

datetime = author_name_list[0].find_all('span',{'class' : 'ml-3 fa fa-clock-o'})
	
print(title.text)
print(author_name_list_items[0].text)
items = author_name_list[0].text.splitlines()
print(items[1].strip())

with open("file.txt", "w") as file:
	file.write(title.text)
	file.write("\n")
	file.write(author_name_list_items[0].text)
	file.write("\n")
	file.write(items[1].strip())


