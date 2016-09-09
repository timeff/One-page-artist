import json
import requests

def wiki_detail(term):
	r = requests.get('https://en.wikipedia.org/w/api.php?action=parse&prop=text&section=0&format=json&page='+term)
	r.json

	data = json.loads(r.text)

	# title=data['query']['pages'].values()[0]['title']
	# extract=data['query']['pages'].values()[0][revisions][0]['contentmodel']
	# # extract=extract[1:40]+"..."


	# temp=[]

	# temp.append(title)
	# temp.append(extract)

	return data

print wiki_detail("john mayer")



