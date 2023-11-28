# https://www.youtube.com/watch?v=kogOfxg1c_g
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi # allow process of html <form> items

tasklist = ['Task1', 'Task2', 'Task3']

TASKLIST_CONTENT = ''
with open('tasklist.html', 'r') as file:
    TASKLIST_CONTENT = file.read()

MANAGETASK_CONTENT = ''
with open('managetasks.html', 'r') as file:
    MANAGETASK_CONTENT = file.read()

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/tasklist'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers() # close headers
            output = TASKLIST_CONTENT
            for task in tasklist:
                output += '<p>%s' % task
                output += '<a href="/tasklist/%s/remove">X</a></p>' % task
            self.wfile.write(output.encode())
        
        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = MANAGETASK_CONTENT
            self.wfile.write(output.encode())
        
        if self.path.endswith('/remove'):
            listIDpath = self.path.split('/')[-2]
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Remove task: %s</h1>' % listIDpath.replace('%20', ' ')
            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/%s/remove">' % listIDpath
            output += '<input type="submit" value="Remove"></form>'
            output += '<a href="/tasklist">Cancel</a>'
            output += '</body></html>'
            self.wfile.write(output.encode())
    
    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, params = cgi.parse_header(self.headers.get('content-type'))
            params['boundary'] = bytes(params['boundary'], "utf-8")
            # handle content length
            # content_length = int(self.headers.get('content-length'))
            # params['CONTENT-LENGTH'] = content_length
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, params)
                new_task = fields.get('task')
                tasklist.append(new_task[0])
        if self.path.endswith('/remove'):
            listIDpath = self.path.split('/')[-2]
            ctype, params = cgi.parse_header(self.headers.get('content-type'))
            params['boundary'] = bytes(params['boundary'], "utf-8")
            if ctype == 'multipart/form-data':
                list_item = listIDpath.replace('%20', ' ')
                tasklist.remove(list_item)
        self.send_response(301) # redirect request
        self.send_header('content-type', 'text/html')
        self.send_header('location', '/tasklist')
        self.end_headers()

def main():
    PORT = 9000
    HOSTNAME = ''
    server = HTTPServer((HOSTNAME, PORT), requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()