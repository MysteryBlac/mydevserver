from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Welcome to my server!")

        elif self.path == "/hello":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Linux!")

        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server is running!")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")


server = HTTPServer(("0.0.0.0", 8000), Server)
print("Server running on port 8000")
server.serve_forever()

