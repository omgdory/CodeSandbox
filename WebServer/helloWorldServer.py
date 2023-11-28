# https://www.youtube.com/watch?v=kogOfxg1c_g
from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers() # close headers
        # wfile is writable file
        self.wfile.write('Hello user'.encode()) # encode so send through http

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers() # close headers
        self.wfile.write(self.path.encode())

def main():
    PORT = 8000
    HOSTNAME = ''
    server = HTTPServer((HOSTNAME, PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()