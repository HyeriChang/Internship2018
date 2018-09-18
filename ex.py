import requests
import json


#print(r.text)
url = 'https://codequs.com/api/post/fetch'
scraped_stores = []

def get_stories_info(self):
		data = {
		'kwd': "",
		'page': "page"
		}
		r = requests.post(self.url, data=data)

		return r.json()[1]['data']
def run(self):
		for page in range(1,10):
			data = self.get_stories_info(page)
			print(json.dumps(data))

#data = json.loads(r.text)
#import pdb; pdb.set_trace()
#1


