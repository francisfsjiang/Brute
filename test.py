import wsgiref.simple_server
import urllib.parse

dict=["REQUEST_METHOD","HTTP_COOKIE","QUERY_STRING","PATH_INFO"]

html="""
<html>
<body>
    <form action="/sign" method="post">
        <textarea name="username" rows="3" cols="60"></textarea>
        <textarea name="password" rows="3" cols="60"></textarea>
        <div><input type="submit" value="Sign Guestbook"></div>
    </form>
    <form action="login.php" method="post">

	<fieldset>

			<label for="user">Username</label> <input type="text" class="loginInput" size="20" name="username"><br />


			<label for="pass">Password</label> <input type="password" class="loginInput" AUTOCOMPLETE="off" size="20" name="password"><br />


			<p class="submit"><input type="submit" value="Login" name="Login"></p>

	</fieldset>

	</form>
</body>
</html>

"""


def mydemo_app(environ,start_response):
    #from io import StringIO
    #stdout = StringIO()
    #print("Hello world!", file=stdout)
    #print(file=stdout)
    #h = sorted(environ.items())
    #for k,v in h:
    #    print(k,'=',repr(v), file=stdout)
    start_response("200 OK", [('Content-Type','text/html; charset=utf-8')])
    text=html
    for i in environ:
        if i in dict:
            #text+=str(i)+" = "+str(environ[i])+"<br/>"
            text+=str(i)+" = "+str(environ[i])+"\n"

    #print(environ.get("CONTENT_LENGTH",0))
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    text+=str(urllib.parse.parse_qs(environ["wsgi.input"].read(request_body_size)))
    #print(environ["wsgi.input"].read)
    print(text)
    return [text.encode("utf-8")]


if __name__=="__main__":
    #sert=wsgiref.simple_server.make_server("localhost",8042,wsgiref.simple_server.demo_app)
    sert=wsgiref.simple_server.make_server("localhost",8042,mydemo_app)
    sert.serve_forever( )