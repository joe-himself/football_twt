import urllib.request
import urllib.parse
import http.cookiejar

url = 'http://courses.iust.ac.ir/login/index.php'

data = urllib.parse.urlencode({'username': "93522072", 'password': 'hihitler'})
data = data.encode('utf-8')

cj = http.cookiejar.CookieJar()



opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
request = urllib.request.Request(url)

request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
request.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0")

response = opener.open(request, data)
respData = response.read().decode('utf-8')

saveFile = open('withHeaders.htm','w')
saveFile.write(str(respData))
saveFile.close()


'''
print("Before")

#print(cj._cookies) #Only for debugging

response.headers.add_header('Set-Cookie',
   'Life=ok; expires=Sat, 17-Aug-2013 06:49:03 GMT; path=/; domain=.bneijt.nl; HttpOnly')
cj.extract_cookies(response, request)
print("After")
print(cj._cookies)









req1 = urllib.request.Request(url)
response = urllib.request.urlopen(req1)
cookie = response.headers.get('Set-Cookie')
resp = urllib.request.urlopen(request, data)
respData = resp.read().decode('utf-8')

saveFile = open('withHeaders.htm','w')
saveFile.write(str(respData))
saveFile.close()
print (str(respData))
#except Exception as e:
 #   print(str(e))
'''
