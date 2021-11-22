import requests
import re
from parsel import Selector
from urllib import parse
from fontTools.ttLib import TTFont


url = 'http://www.porters.vip/confusion/movie.html'
resp = requests.get(url)
sel = Selector(resp.text)
css_path = sel.css('link[re=stylesheet]')