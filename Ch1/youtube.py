import json
from urllib.request import urlopen 
#url = "https://gdata.youtube.com/feeds/api.standardfeeds/top_rated?alt=json"
url = "http://www.bilibili.com/video/av9283218/?tg"
response = urlopen(url)   #链接指定地址处的Web服务器并请求指定的Web服务
contents = response.read()#获取响应数据并赋值给变量contents
text = contents.decode('utf-8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
	print(video['title']['$t'])