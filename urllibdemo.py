# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
import http
import urllib.parse
import urllib.request
import urllib
from urllib import request
from urllib import parse


#只是read返回的是二进制数据，记得编码
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

# 这个并不能加header的，它传的是form表单
# ip在http请求中不能更改
data = bytes(urllib.parse.urlencode({'word': 'hello',"origin": "121.28.97.251"}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# 没有header
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

# 获取响应头，响应体，响应的内容
response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(response.read().decode('utf-8'))


# request对象
# 加header
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 第二中加header
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))





# open函数可以接收request对象
# cookie维持登陆状态
# 获取cookie，但是不能保存
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)


# 获取cookie，并且保存读取
# MozillaCookieJar是cookiejar的子类可以有保存，加载方法。
# 获取cookie的另一种方法LWPCookieJar，用那种方式读存要一致
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))


# 添加代理
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())



from urllib.parse import urlparse
from urllib.parse import urljoin

# url拆分
# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# 指定请求协议，当然如果前面有，不会强求
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
#  ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
print(type(result), result)

# url合并
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urllib.urlunparse(data))

# url合并:以后面为主，后面有的看后面，后面没有的前面补
# 少域名的时候可用,
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))


from urllib.parse import urlencode
# url传参 把字典直接变成参数
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)