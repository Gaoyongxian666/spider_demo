# encoding: utf-8
'''
@author: gaoyongxian666
@file: beautifulsoupdemo.py
@time: 2018/4/10 19:19
'''
from lxml.html.clean import unicode

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
#
print(soup.prettify())


# 获取节点，string就是标签里的内容
print(soup.title.string)
# 节点都是<class 'bs4.element.Tag'>
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)

# 获取节点的属性，节点只会选择第一个
print(soup.p.attrs['name'])
print(soup.p['name'])
# 嵌套使用标签选择器
print(soup.head.title.string)
# 获取文档中所有内容
print(soup.get_text())


# 四种对象：Tag , NavigableString , BeautifulSoup , Comment .


# tag中最重要的属性: name和attributes
# 节点就是<class 'bs4.element.Tag'>
tag=soup.title
tag['class']
# 获取单个，所有
tag.attrs
# {u'class': u'boldest'}
# tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样，更改了就会影响beautisoup对象
tag['class'] = 'verybold'
tag['id'] = 1
tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>
del tag['class']
del tag['id']
tag
# <blockquote>Extremely bold</blockquote>
tag['class']
# KeyError: 'class'
print(tag.get('class'))
# None
# 多值更改tag
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
rel_soup.a['rel']
rel_soup.a['rel'] = ['index', 'contents']

# NavigableString
# 转成Unicode编码
unicode_string = unicode(tag.string)
unicode_string
# 更改tag包含的字符串
tag.string.replace_with("No longer bold")


# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,


# Comment 对象是一个特殊类型的 NavigableString 对象:注释



# 操作文档树
# tag的 .contents 属性可以将tag的子节点以列表的方式输出:（上面的四种对象）

# 通过tag的 .children 生成器,可以对tag的子节点进行循环:
# for child in title_tag.children:

# .descendants 属性可以对所有tag的子孙节点进行递归循环 [5] :
# for child in head_tag.descendants:
#     print(child)
    # <title>The Dormouse's story</title>
    # The Dormouse's story

# 注意这是两个节点
# head_tag.contents
# [<title>The Dormouse's story</title>]
# head_tag.string
# u'The Dormouse's story'

# 如果tag中包含多个字符串 ,可以使用 .strings 来循环获取:遍历的是这个tag中所有的字符串对象
# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:全部是空格的行会被忽略掉,段首和段末的空白会被删除

# 搜寻树
# 找所有包含t的标签
# soup.find_all(re.compile("t")):
# 找出所有的a,b标签
# soup.find_all(["a", "b"])
# soup.find_all(href=re.compile("elsie"))
# 可以指定属性
# soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# 查找所有包含 id 属性的tag,无论 id 的值是什么:
# soup.find_all(id=True)
# css选择器
# soup.select("title")

# 如果只想得到tag中包含的文本内容,那么可以嗲用 get_text() 方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回:

