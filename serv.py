import socket 
import threading
import time

LOCAL_IP = '192.168.1.8'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCAL_IP, PORT))
server.listen()

connections = []
usernames = []

def broadcast(message):
    for connection in connections:
        connection.send(message)


def receive():
    while True:
        conn, addr = server.accept()
        print(f'Connected with: {addr}')
        conn.send("username".encode("utf-8"))
        username = conn.recv(1026).decode("utf-8")
        print(f'Connected with username {username}')
        usernames.append(username)
        connections.append(conn)
        conn.send("Connected to the server successfully!".encode("utf-8"))


        thread = threading.Thread(target=handle, args=(conn,))
        thread.daemon = True
        thread.start()


def handle(client):
    while True:
        try:
            message = client.recv(1026)
            broadcast(message)
            time.sleep(2)
        except:
            index = connections.index(client)
            connections.remove(client)
            client.close()
            username = usernames[index]
            print(f'{username} has left the chat')
            broadcast(f'{username} has left the chat'.encode("utf-8"))
            usernames.remove(username)
            break


print("[+] server is online...")
time.sleep(1)
print("[+] waiting on connections...")
time.sleep(1)
receive()