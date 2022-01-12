import socket


if __name__ == "__main__":
    class szinek:
        yellow = "\33[33m\33[1m"
        blue = "\33[34m\33[1m"
        white = "\33[0m"
        green = "\33[32m"
        red = "\33[31m\33[1m"
    # For tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    IPs = [
        
    ]


    host= "192.168.1.3"; port=8000


    sock.bind((host,port))
    # Number of backlog clients
    sock.listen(100)

    print (szinek.green + " \t\t\t\tSERVER WORKING \33[0m" )
    print(szinek.yellow+"IP: "+ szinek.blue + host + szinek.white)
    print(szinek.yellow+"Port: "+ szinek.blue + str(port) + szinek.white)

    while True:
        (client, (ip, port)) = sock.accept()
        IPs.append(ip)
        print (szinek.yellow + "Új kliens csatlakozva. " + szinek.green +  "IP: " + szinek.blue + "{}".format(ip) + szinek.green + " Port: " + szinek.blue + "{}".format(port) + szinek.white)
        data = client.recv(2048)
        while len(data):
            message = data.decode()
            if (message.startswith("/setusername")):
                IPs.append("{}".format(ip,message))
                #print(IPs[message] + " changed username to:" + message)
                print(IPs)
            else:
                if (message == "/quit"):
                    data = client.recv(2048)
                    sock.close()
                    print(szinek.red + "User: " + "{}".format(IPs) +" Diconnected." + szinek.white)
                    break
                elif(message == "/reconnect"):
                    sock.close()
                    (client, (ip, port)) = sock.accept()
                elif(message == "/ping"):
                    client.send("kurva".encode())
                    data = client.recv(2048)
                    continue
                elif(not message.startswith("/")):
                    print (szinek.yellow + "User: " + szinek.blue + "{}".format(IPs) + szinek.yellow + " Sent Message : " + szinek.green + message + szinek.white)
                    client.send(data.upper())
                    data = client.recv(2048)


    print ("Closing the Socket!!")
    sock.close()