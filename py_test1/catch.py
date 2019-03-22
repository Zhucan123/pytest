import requests
from bs4 import BeautifulSoup


def get_html(url):
    """get connect"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def get_content(html):
    """get content"""
    soup = BeautifulSoup(html, features='html.parser')
    content = soup.select('div.content')
    return content


# 总共有几种类型的文章
pageType = ["hot", "textnew", "text", "history"]


def get_page_content(page_type, _page):
    # 这个是每行的字数
    content_size = 50
    c_url = "https://www.qiushibaike.com/"+page_type+"/page/" + str(_page) + "/"
    c_html = get_html(c_url)
    c_content = get_content(c_html)
    # 循环遍历每一段内容
    for x in c_content:
        text = x.get_text()
        length = len(text)
        print("<<<<<<<<<<<<<_______________>>>>>>>>>>>>")
        for y in range(length):
            if y % content_size == 0 and y > 1:
                print(text[y - content_size: y])
            if y == length - 1:
                print(text[(length - length % content_size): length])
    if "下一页" in c_html:
        # 如果有下一页,就递归获取下一页
        _page += 1
        print("这个是第"+str(_page)+"页!!!")
        get_page_content(page_type, _page)
    else:
        print("已获取完所有的页面!!!")


# 开启页面内容获取
for y in pageType:
    get_page_content(y, 1)


