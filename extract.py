import json
from pprint import pprint

with open('raw_emojis.json') as data_file:    
    raw = json.load(data_file)


with open('old_formatted.json') as data_file:    
    old = json.load(data_file)

with open('categories_raw.json') as data_file:    
    categories = json.load(data_file)


new = {}

for shortcode, value in old.items():
	found = False
	for alt, code in raw.items():
		if alt == value["alt"]:
			new[shortcode] = {
				"class": "emoji " + code,
				"alt": alt
			}

			for category, catObj in categories.items():
				if code in catObj["emoji"]:
					new[shortcode]["class"] = code + " " + catObj["category"] + " emoji"
					break

			found = True
			break

	if not found:
		new["not-found-"+shortcode] = {
				"class": "emoji" + code,
				"alt": alt
			}

print(new)

# with open('icons.json', 'w') as fp:
#     json.dump(new, fp)