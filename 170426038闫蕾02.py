import urllib.request
url='http://www.taobao.com'
proxy_handle={'http':'http://222.95.16.235:9999'
              'http':'http://60.205.57.4:9999' 
 }
proxy=urllib.request.ProxyHandler(proxy_handle)
opener=urllib.request.build_opener(proxy)
response=opener.open(url)
print(response.read()，decode('utf8'))