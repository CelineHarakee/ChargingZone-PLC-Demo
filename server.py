from http.server import BaseHTTPRequestHandler, HTTPServer

class CaptivePortalHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/generate_204", "/gen_204", "/ncsi.txt", "/connecttest.txt"]:
            self.send_response(204)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

def run():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, CaptivePortalHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
