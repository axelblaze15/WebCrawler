import requests
from bs4 import BeautifulSoup
import time, urllib
from urlparse import urljoin

def find_first_link(url):
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html,'html.parser')

	big_div = soup.find(id = "mw-content-text").find(class_="mw-parser-output")

	first_link = None
	for element in big_div.find_all('p',recursive=False):
		if element.a:
			first_link = element.a.get('href')
			break

	if not first_link:
		return

	first_link = urljoin('https://en.wikipedia.org/',first_link)

	return first_link


def continue_crawl(search_history, target_url):
	if len(search_history) > 25:
	    return False
	    #pass
	if search_history[-1] == target_url:
	    return False
	        #pass
	visited = {}
	for key in search_history:
	    if not visited.get(key):
	        visited[key] = 1
	    else:
	        return False
	return True

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

search_history = [start_url]

while continue_crawl(search_history, target_url):
	print search_history[-1]
	first_link = find_first_link(search_history[-1])
	if not first_link:
		print "Ending Found but target_url not found"
		break
	search_history.append(first_link)
	time.sleep(2)
