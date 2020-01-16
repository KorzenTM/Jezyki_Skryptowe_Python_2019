import urllib.request

try:
    site = urllib.request.urlopen("https://www.youtube.com/")
except:
    print("Site does not exits!")
else:
    meta = site.info()
    print (meta)