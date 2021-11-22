import requests
import re
from parsel import Selector
from urllib import parse
from fontTools.ttLib import TTFont


url = 'http://www.porters.vip/confusion/movie.html'
resp = requests.get(url)
sel = Selector(resp.text)
css_path = sel.css('link[rel=stylesheet]::attr(href)').extract()
print(css_path)
woffs = []
for c in css_path:
    css_url = parse.urljoin(url, c)
    css_resp = requests.get(css_url)
    woff_path = re.findall("src:url\('..(.*.woff)'\) format\('woff'\);", css_resp.text)
    print(woff_path)
    if woff_path:
        woffs += woff_path
print(woffs)
woff_url = 'http://www.porters.vip/confusion/' + woffs.pop()
woff = requests.get(woff_url)
filename = './woff/target.woff'
with open(filename, 'wb') as f:
    f.write(woff.content)
