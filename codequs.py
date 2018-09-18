import requests
import json


#print(r.text)

r = requests.post("https://codequs.com/api/post/fetch", json={'page': 0, 'kwd': ""})

data = json.loads(r.text)
#import pdb; pdb.set_trace()
#1
print(json.dumps(data).split("/n"))
