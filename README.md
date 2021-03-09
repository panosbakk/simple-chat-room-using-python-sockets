# simple-chat-room-using-python-sockets
This project is basically a chat room using the server-client model, with TCP protocol

#Usage:

First, you need to run the serv.py file. You can do it by going to CMD(or terminal for Mac/Linux) and typing python3 serv.py .
While the server is running, you can use the client.py file to connect to the server and start chatting with anyone that is connected to it.
You can do that by again going to cmd(or terminal) and typing python3 client.py .
If you want to exit the server, you can just hold at the same time Ctrl + C. For the server to close, you have to close the window.
Disclaimer: The code as it is runs on your local machine. If you want to modify it in order to run it on LAN, you will have to change the server's IP Address to your local machine, and also modify the client with the same IP.
If you want to run it on the Internet(have people run it outside your local area network) then you would have to modify the client side script and put your public IP Address on it, but you will also have to do portforwarding on the specific port.


