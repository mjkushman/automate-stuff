#! Python 3
#downloadXkcd.py - downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com' 	#starting url
os.makedirs('xkcd', exist_ok=True) 		#store comics in ./xkcd
while not url.endswith('#'):
	#TODO: download the page -- DONE
	print('Downloading page: %s' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	#TODO find the url of the comic image
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		try:
			comicUrl = 'https:' + comicElem[0].get('src')
			#download the image
			print('Downloading image: %s' %(comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exception.MissingSchema:
			#skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'https://xkcd.com' + prevLink.get('href')



	#TODO: save the image to ./xkcd
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	#TODO: get the prev button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + prevLink.get('href')


print('Done')
