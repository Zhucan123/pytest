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


c_url = "https://www.qiushibaike.com/hot/"
c_html = get_html(c_url)
c_content = get_content(c_html)
page_Index = 50

for x in c_content:
    text = x.get_text()
    length = len(text)
    print("<<<<<<<<<<<<<_______________>>>>>>>>>>>>")
    for y in range(length):
        if y % page_Index == 0 and y > 1:
            print(text[y-page_Index: y])
        if y == length-1:
            print(text[(length-length % page_Index): length])
