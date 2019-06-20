import urllib.request
url='http://www.taobao.com'
proxy_handle={'http':'http://222.95.16.235:9999'
              'http':'http://60.205.57.4:9999' 
 }
proxy=urllib.request.ProxyHandler(proxy_handle)
opener=urllib.request.build_opener(proxy)
response=opener.open(url)
print(response.read()，decode('utf8'))

import http.cookiejar,urllib.request
cookie=http.cookiejar.CookieJar()
cookie = http.cookiejar.MozillaCookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.taobao_opener(handler)
url='http:www.taobao.com'
request = urllib.request.Request(url,headers=headers)
response=opener.open('http:www.taobao.com')
for item in cookie:
    print(item.name,item.value)
    filename = 'yl.txt'
    cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load('yl.txt')
    print(cookie)
