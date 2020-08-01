import socketserver
import xml.etree.ElementTree as xml

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        test = self.data.decode("utf-8")
        print("{} wrote:".format(self.client_address[0]))
        print(test)
        
        #test the xml parsing with etree
        root = xml.fromstring(test)
        for dummy in root.iter('playerName'):
            print(dummy.text)
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 11750

    # Create the server, binding to localhost on port 101
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()