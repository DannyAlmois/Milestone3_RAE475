import SocketServer #library
from telnetsrv.threaded import TelnetHandler, command #library

class MyHandler(TelnetHandler): #class and commands

        WELCOME = "This is Telnet server"
        @command('version')
        def version(self, params): #parametr
         self.writeresponce("V0.1")

class TelnetServer(SocketServer.TCPServer): #server definition
    allow_reuse_address = True

server = TelnetServer(("10.0.10.100", 10023), MyHandler) #server definition
server.serve_forever() #request
