import socket
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

HOST = "0.0.0.0"
HTTP_PORT = 3000
SOCKET_HOST = "socket_server"
SOCKET_PORT = 5000


def send_to_socket(data: dict):
    """Send form data to socket server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SOCKET_HOST, SOCKET_PORT))
    client.send(str(data).encode())
    client.close()


class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path in ["/", "/index"]:
            self.send_html("templates/index.html")
        elif self.path == "/message":
            self.send_html("templates/message.html")
        elif self.path.startswith("/static/"):
            self.send_static()
        else:
            self.send_html("templates/error.html", 404)

    def do_POST(self):
        if self.path == "/message":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length).decode()

            data = urllib.parse.parse_qs(body)
            message = {
                "username": data.get("username", [""])[0],
                "message": data.get("message", [""])[0]
            }

            send_to_socket(message)

            self.send_response(302)
            self.send_header("Location", "/message")
            self.end_headers()

    def send_html(self, filename, status=200):
        try:
            with open(filename, "rb") as f:
                content = f.read()

            self.send_response(status)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404)

    def send_static(self):
        file_path = self.path.lstrip("/")
        try:
            with open(file_path, "rb") as f:
                self.send_response(200)
                if file_path.endswith(".css"):
                    self.send_header("Content-type", "text/css")
                elif file_path.endswith(".png"):
                    self.send_header("Content-type", "image/png")
                self.end_headers()
                self.wfile.write(f.read())
        except:
            self.send_error(404)


def run():
    server = HTTPServer((HOST, HTTP_PORT), SimpleHandler)
    print(f"HTTP running on {HTTP_PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()