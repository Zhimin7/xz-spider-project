from fontTools.ttLib import TTFont


font = TTFont('./woff/movie.woff')
font.saveXML('./woff/movie.xml')