#!/usr/bin/env python
#Hmmm... http://www.endclothing.com/media/us_sitemap.xml

import urllib2, zlib, json
url='https://launches.endclothing.com/api/products'
req = urllib2.Request(url)
req.add_header(':host','launches.endclothing.com');req.add_header(':method','GET');req.add_header(':path','/api/products');req.add_header(':scheme','https');req.add_header(':version','HTTP/1.1');req.add_header('accept','application/json, text/plain, */*');req.add_header('accept-encoding','gzip,deflate');req.add_header('accept-language','en-US,en;q=0.8');req.add_header('cache-control','max-age=0');req.add_header('cookie','__/');req.add_header('user-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36');
resp = urllib2.urlopen(req).read()
resp = zlib.decompress(bytes(bytearray(resp)),15+32)
data = json.loads(resp)
for product in data:
	for attrib in product.keys():
		print str(attrib)+' :: '+ str(product[attrib])
	print '\n'
