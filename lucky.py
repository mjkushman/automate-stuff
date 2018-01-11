#! python 3
#lucky.py - performs a google search 
# and opens the first 3 results in separate tabs

import requests, sys, webbrowser, bs4, pprint

print('Googling...') #display text while downloading the google page

res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:])) #search term will be specified by system arguments
res.raise_for_status()

#TODO: retriee top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElms = soup.select('.r a') #grabs <a> elemnts within .r class


#TODO open a broswer tab for each result
numOpen = min(3, len(linkElms))
for i in range(numOpen):
	#pprint.pprint(linkElms[i])
	webbrowser.open('https://google.com' + linkElms[i].get('href'))