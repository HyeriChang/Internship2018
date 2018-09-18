import requests
import bleach
import yaml
from bs4 import BeautifulSoup
from __future__ import unicode_literals

page = requests.get('https://realpython.com/')
soup = BeautifulSoup(page.text, 'html.parser')


with open("config.yaml", 'r') as f:
	doc = yaml.load(f)

	#get value of all class
	txt1 = doc["block_list"]["div"]["class"]
	#remove [] & x=col-12 col-md-6 col-lg-4 mb-5
	x = " ".join(map(str, txt1))

	# y = a
	txt2 = doc["block_list"]["block"]["links_text"]
	y = " ".join(map(str, txt2))
	#print(y)

	# z = card-title h4 my-0 py-0
	txt3 = doc["block_list"]["block"]["title_list_2"]["h2"]["class"]
	z = " ".join(map(str, txt3))

	# g = href
	txt4 = doc["block_list"]["block"]["links"]["links_text"]
	g = " ".join(map(str, txt4))

	# k = text-muted
	txt5 = doc["block_list"]["block"]["datetime_list"]["small"]["class"]
	g = " ".join(map(str, txt5))

block_list = soup.find_all('div', {'class' : x})
with open("file2.txt", "w") as file:
	for block in block_list:
		
		#find all path link go to detail tutorial start with <a>
		links_text = block.find(y)

		#find all title tutorial start with <h2 class>
		title_list_2 = block.find('h2', {'class': z})

		#create new url for each tutorial transplate with main url
		links = 'https://realpython.com'+ links_text.get('href')
		
		#find datetime
		datetime_list = block.find('small',{'class' : g})

################################
		
		print( "title: ", title_list_2.text)
		print("url: ", links)
		#lay cai tag ra truoc sau do remove ra cai span r in cái span.text ra 
		tags = block.find_all('a',{'class': 'badge'})
		print("tag: ",end="	")
		for tag in tags:
			tag.extract()
			print(tag.text,end=" ")

		#check tutorial have datetime
		#strip() xoa cac khoang trang duoc in ra
		x = datetime_list.text.replace('\n',' ').strip()
		if x:
			print("\ndate: ", x)
		print("\n")


		file.write("\ntitle: " + title_list_2.text)
		file.write("\n")
		file.write("url: " + links)
		file.write("\n")

		file.write("tag: ")
		for tag in tags: 
			file.write(tag.text+" ")

		if x:
			file.write("\ndate: " + x)
		file.write("\n")

		
		
		
		