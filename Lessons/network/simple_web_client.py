import socket


server = "google.com"

print("Connect to google.com ...")
with socket.create_connection((server, 80)) as s:
    print("Sending request...")
    s.sendall(b"""
GET / HTTP/1.1
Host: www.google.com
Accept-Language: en

""")

    print("Getting response from server...")
    print("Got response:")
    data = s.recv(1024)
    print(data.decode("utf-8"))

