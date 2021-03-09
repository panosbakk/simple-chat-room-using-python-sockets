import socket
import threading
import time
import sys



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '127.0.0.1'
PORT = 4444
try:
    client.connect((IP, PORT))
    username = input("Username: ")
except socket.error:
    print("Connection timed out, probably host is down")
    client.close()
    sys.exit()


def receive_from_server():
    while True:
        try:
            message = client.recv(1026).decode("utf-8")
            if message == "username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            client.close()
            break

def send_msg():
    while True:
        try:
            message = f'{username} >>> {input("")}'
            client.send(message.encode("utf-8"))    
        except:
            client.close()
            break
            

receivingthread = threading.Thread(target=receive_from_server)
receivingthread.daemon = True
receivingthread.start()

try:
  sendthread=threading.Thread(target=send_msg)
  sendthread.daemon=True
  sendthread.start()
  while True: time.sleep(100)
except (KeyboardInterrupt, SystemExit):
  print ("You have forcibly closed your connection to the server. Hope to see you soon!")
