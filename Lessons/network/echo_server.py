import socket

HOST = "127.0.0.1"
PORT = 5454

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Starting server on {}:{}".format(HOST, PORT))
    s.bind((HOST, PORT))
    s.listen()

    running = True
    while running:
        conn, addr = s.accept()

        with conn:
            print("Client connected from {}".format(addr))

            while True:
                data = conn.recv(1024)

                if not data:
                    break

                if data == b"quit":
                    running = False

                print("Got from client:", data)
                conn.sendall(data.decode('utf-8').upper().encode('utf-8'))
