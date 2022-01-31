import socket

HOST = "127.0.0.1"
PORT = 5454

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Connecting to the server {}:{}".format(HOST, PORT))
    s.connect((HOST, PORT))
    
    data = input("Your message: ")
    print("Sending '{}'...".format(data))
    s.sendall(data.encode('utf-8'))

    print("Getting response from server...")
    data = s.recv(1024)
    print("Got from server:", data)
