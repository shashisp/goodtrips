import requests

API_KEY = 'b0021c54-5990-4e13-b060-ed7f92f93081'
URL = 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1'

def analyze_text(text):
	new_url = URL+'?text='+text+'&apikey='+API_KEY
	res = requests.post(new_url)
	return res.json()['aggregate']['score']

