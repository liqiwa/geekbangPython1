from urllib import  request
url = 'http://www.baidu.com'
reponse  = request.urlopen(url,timeout=1)
print(reponse.read().decode('utf-8'))