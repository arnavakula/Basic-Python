import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.python.org/static/img/python-logo@2x.png'

urllib.request.urlretrieve(url, 'pythonlogo.png')