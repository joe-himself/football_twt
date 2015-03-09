import urllib.request
import urllib.parse
import http.cookiejar

#try:
#headers = {}
#headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

url = 'http://courses.iust.ac.ir/login/index.php'


data = urllib.parse.urlencode({'username': "93522072", 'password': 'hihitler', 'rememberusername':'0'})
data = data.encode('utf-8')


request = urllib.request.Request(url)

req1 = urllib.request.Request(url)
response = urllib.request.urlopen(req1)
cookie = response.headers.get('Set-Cookie')
request.add_header('Cookie', cookie)
request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
request.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0")
resp = urllib.request.urlopen(request, data)
respData = resp.read().decode('utf-8')

saveFile = open('withHeaders.htm','w')
saveFile.write(str(respData))
saveFile.close()
print (str(respData))
#except Exception as e:
 #   print(str(e))



