import http.server
import socketserver


PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

# サーバを起動
def startServer():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
