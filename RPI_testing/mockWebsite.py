from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps({"hour": 15, "minute": 41, "song": "Never Give Up"}), "utf-8"))

    
def main():
    port = 9000;
    serverAddress = ('localhost', port)
    server = HTTPServer(serverAddress, requestHandler)
    print("Server started on port: " + str(port))
    server.serve_forever()


if __name__ == "__main__":
    main()