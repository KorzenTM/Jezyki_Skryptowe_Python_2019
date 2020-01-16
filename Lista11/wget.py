import sys 
import urllib.request

def findTitle(url):
    webpage=urllib.request.urlopen(url).read()
    title=str(webpage).split('<title>')[1].split('</title>')[0]
    return title

url=str(sys.argv[1])
print(url)
print(url[23])
name=findTitle(url)

if url[23]=="/":
    urllib.request.urlretrieve(url,"index.html")
else:
    urllib.request.urlretrieve(url,"%s.html" %(name))

