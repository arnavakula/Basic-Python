import urllib.request
import urllib.error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

try:
    url = urllib.request.urlopen("https://www.python.org/")
    content = url.read()
except:
    print("404 web page not found")
    exit()
    
f = open('python.html', 'wb')
f.write(content)
f.close()

urllib.request.urlopen("https://www.python.org/")