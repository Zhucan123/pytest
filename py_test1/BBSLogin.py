import requests
import re


def get_content(url):
    html = requests.get(url)
    return html.content


def get_xsrf(url):
    content = get_content(url)
    patten = re.compile('.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?')
    match = re.findall(patten, content)
    xsrf = match[0]
    return xsrf


#登陆
def login(baseurl, email, password):
    login_data = {
        '_xsrf': get_xsrf(baseurl),
        'password': password,
        'remember_me': 'true',
        'email': email
    }

    headers_base = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        'Referer': 'http://www.zhihu.com/',
    }

    session = requests.session()
    baseurl += "/login/email"
    content = session.post(baseurl, headers=headers_base, data=login_data)
    print(content.text)
    s = session.get("http://www.zhihu.com", verify=False)
    print(s.text.encode('utf-8'))
    f = open("zhihu.txt", 'w')
    f.write(s.text.encode('utf-8'))


url_ = "http://www.zhihu.com"
login(url_, '13995921623', 'zc1314520')
