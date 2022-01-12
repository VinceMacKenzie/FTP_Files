
__author__ = 'uva'
from os import times
import socket
import getpass

class szinek:
        yellow = "\33[33m\33[1m"
        blue = "\33[34m\33[1m"
        white = "\33[0m"
        green = "\33[32m"
        red = "\33[31m\33[1m"

sock = socket.socket()
data=""



username = getpass.getuser()
print("Username: "+ username)

def login():
   host = "poryder.hu"
   port = 8000
   sock.connect((host, port))
   print(szinek.green + "Sikeres csatlakozás a szerverhez!" + szinek.white)
login()
sock.send(username.encode())
while(data != "/quit"):
   data = input(szinek.blue + "Chat: " + szinek.white)
   if (data == "/reconnect"):
      sock.close()
      login()
   elif(data == "/ping"):
      sock.send(data.encode())
      received = sock.recv(2048)
      print(received.decode())
   else: # Elküldi a szervernek az üzenetet.
      try:
         sock.send(data.encode())
         received = sock.recv(2048)
      except Exception as e:
         print (e)
print(szinek.red + "Kilépve." + szinek.white)
quit()

print('Sent data :{} '.format(data))

#try / exceptet def ciklussá tenni.