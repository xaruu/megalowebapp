import requests
from bs4 import BeautifulSoup

def getlink(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	wiz = soup.findAll("c-wiz")
	link = wiz[6]['data-url']

	return link
