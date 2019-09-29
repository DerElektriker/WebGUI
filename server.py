#! /home/matias/.pyenv/versions/WebServer/bin/python
import http.server
from http.server import HTTPStatus
import socketserver
import re,os

PORT = 8080


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        f = None

        print(self.path)
        a=re.match(".*/suche\?item=(?P<item>.*)",self.path)
        if a:
            f= open("/home/matias/Downloads/Untitled Diagram.svg","rb")   
            fs = os.fstat(f.fileno())
            ctype = "image/svg+xml"


            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", ctype)
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified",
                self.date_time_string(fs.st_mtime))
            self.end_headers()

            

        if not f:
            f = self.send_head()

        if f:
            try:
                self.copyfile(f, self.wfile)
            except:
                print("It didnt work")
            finally:
                f.close()

Handler = MyHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()