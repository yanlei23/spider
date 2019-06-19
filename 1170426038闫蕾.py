def myadd(a=1,b=100):
result = 0
i = a
while i <= b: 
result += i
i += 1
return result
print myadd(1,10)
print myadd() 
print myad

data = bytes(urllib.parse.urlencode({'pw':'444','un':'777'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
print(result)



