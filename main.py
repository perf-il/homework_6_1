from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_answer(self):
        return 'Hello, World wide web!'

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "any")
        self.end_headers()
        self.wfile.write(bytes(self.__get_answer(), "utf-8"))

    def do_POST(self):
        client_len = int(self.headers.get('Content-Length'))
        client_data = self.rfile.read(client_len)
        print(client_data.decode())

        self.send_response(200)
        self.send_header("Content-type", "any")
        self.end_headers()
        self.wfile.write(bytes(self.__get_answer(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")