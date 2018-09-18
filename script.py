import yaml

with open("config.yaml", 'r') as f:
	doc = yaml.load(f)

	txt1 = doc["block_list"]["div"]["class"]
	print(" ".join(map(str, txt1)))

	txt2 = doc["block_list"]["block"]["links_text"]
	print("".join(map(str, txt2)))

	txt3 = doc["block_list"]["block"]["title_list_2"]["h2"]["class"]
	print("".join(map(str, txt3)))

	#txt4 = doc["block_list"]["block"]["links_text"]["links"]
	#print("".join(map(str, txt4)))

	txt5 = doc["block_list"]["block"]["datetime_list"]["small"]["class"]
	print("".join(map(str, txt5)))

