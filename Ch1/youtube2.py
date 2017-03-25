#用requests重写的youtube.py

import requests
#url = "https://gdata.youtube.com/feeds/api.standardfeeds/top_rated?alt=json"
url = "http://www.bilibili.com/video/av9283218/?tg"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
	print(video['title']['$t'])