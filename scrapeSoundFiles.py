from bs4 import BeautifulSoup as bs
import requests
import wget

url = 'http://songsofinsects.com/'
response = requests.get(url,timeout=5)
content = bs(response.content, "html.parser")

linkSpans = content.findAll("span",attrs = {'style':'padding-left: 10px;'})

linkList = []

for span in linkSpans:
    link = span.findAll("a")
    linkList.append(link[0]["href"])

downloadList = []
for link in linkList:
    response = requests.get(link,timeout=5)
    content = bs(response.content,"html.parser")
    audio = content.find("source",type="audio/mpeg")
    if( audio != None):
        downloadList.append(audio["src"])

for url in downloadList:
    wget.download(url)
