import requests
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response=requests.get(url)
HTML=res.text
URLS=HTML.split('\n')
for url in URLS:
            tt=url.split('/')[-1]
            response=requests.get(url)
            content = response.content
with open(tt,'wb') as f:
        f.write(content)

str_ = open('res1.txt'，"rb").read()
results = res1.findall('http://www.hao123.com/s?',s)
open("urls.txt","wb").write("\r\n".joint(results))





    
