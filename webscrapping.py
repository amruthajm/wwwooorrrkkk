import requests
from bs4 import BeautifulSoup
search="fifa"
url="http://www.google.com/search?q=" + search
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
g_data = soup.select(" .r a")
for item in g_data:
	print(item.text)
 

