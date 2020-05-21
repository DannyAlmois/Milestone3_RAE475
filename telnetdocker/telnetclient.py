import telnetlib #library

HOST = '10.0.10.100' #ip address of server
PORT = 10023

tn = telnetlib.Telnet(HOST, PORT) #interface definition
tn.set_debuglevel(100) #level of error
data = tn.read_until("custom server", timeout=1) #parametry definition
print ("Data: " + data)
tn.close() #interface closing


