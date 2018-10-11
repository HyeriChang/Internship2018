# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import bleach
import yaml
from bs4 import BeautifulSoup
import pdb; pdb.set_trace()

page = requests.get('https://realpython.com/')
soup = BeautifulSoup(page.text, 'html.parser')

block_list = soup.find_all('a', {'class' : 'card-image'})

#print (block_list)
with open("scotch.txt", "w") as file:
  for block in block_list:
    #tim xem href co trong the a hay khong? neu co thi in ra||ko thi phai tim the a r ms get href
    links_text = block.get('href')
    if links_text == None :
        links_text = block.find('a')
        print("url: ",links_text.get('href') )
    else:
        print("url: ",links_text)

    title_list = block.get('title')
    if title_list == None:
        title_list = block.find('h2', {'class': 'card-title h4 my-0 py-0'})
        print("title: ", title_list)
    else:
        print("title: ", title_list)
