import socketserver
import xml.etree.ElementTree as xml
import Message

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
        
        #deserialize the message
        receivedMessage = Message.deserialize(test)
        print(receivedMessage.messageType)
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 11750

    #test the serialization
    myMessage = Message.DummyMessage()
    test = Message.serialize(myMessage)
    print(test)

    #test the deserialization
    testString = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="18">
<messageType>38</messageType>
<message>helloworld V2</message>
</boost_serialization>"""
    deserialized = Message.deserialize(testString)

    # Create the server, binding to localhost on port 101
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()