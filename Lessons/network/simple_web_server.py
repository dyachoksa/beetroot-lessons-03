import socket

HOST = "127.0.0.1"
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)

    print(f'Serving HTTP on port {PORT} ...')

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)

        print("Client connected:", addr)
        print("Got from client:\n", data.decode("utf-8"))

        http_response = b"""\
HTTP/1.1 200 OK

<h1>Hello, World!</h1>

<p>Recusandae proident mollis, architecto fames bibendum ultricies asperiores
praesent aspernatur, excepturi, dignissimos, quisquam viverra, commodi,
minima, fames adipisicing. Labore dolore, aliquid porta ducimus expedita vestibulum.</p>

<p>Architecto dolore id molestie et sem dicta, irure eaque, maxime soluta
expedita, primis interdum dictumst lacus? Do atque, dictum expedita, rhoncus!
Diamlorem bibendum unde, laoreet.</p>
"""
        conn.sendall(http_response)
        conn.close()
