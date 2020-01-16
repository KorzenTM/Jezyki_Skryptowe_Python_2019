import re
text = 'Contents:https://w3resource.com \n Python Examples: http://github.com Even More Examples'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)