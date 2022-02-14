from base64 import decode
import threading
import socket
import signal

__version__ = "1.0.1"

name = "Tweety"


class Server:
    def __init__(self, addr: str, port: int) -> None:
        self.addr = addr
        self.port = port
        self.clients = []
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.running = True

    def shutdown(self):
        print("Server is about to shutdown...")
        self.running = False

        for client in self.clients:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
    
    def run(self):
        # bind for specific address and port
        self.server_socket.bind((self.addr, self.port))
        # maximum number of active connections
        self.server_socket.listen(100)

        print("Server started at {}:{}".format(self.addr, self.port))
        print("Waiting for client connections...")

        while self.running:
            # accept client connection
            conn, client_addr = self.server_socket.accept()

            self.clients.append(conn)

            print("Client {} connected.".format(client_addr))

            threading.Thread(target=self.handle_client, args=(conn, client_addr)).start()
    
    def handle_client(self, conn, addr):
        """Handle client connection"""
        print("Thread id:", threading.get_native_id())
        conn.send(("Welcome to {}/{}".format(name, __version__)).encode("utf-8"))
        conn.send(b"[NAME]")

        client_name = conn.recv(512).decode("utf-8")
        self.broadcast("{} connected!".format(client_name))
        
        while True:
            message = conn.recv(2048)
            print("Got message from <{}>:".format(client_name), message.decode("utf-8"))
            
            self.broadcast("<{}>: {}".format(client_name, message.decode("utf-8")))
    
    def broadcast(self, message):
        for client in self.clients:
            # possible todo: don't send back to the original client
            client.send(message.encode("utf-8"))


def main():
    addr = "127.0.0.1"
    port = 8899

    server = Server(addr, port)

    signal.signal(signal.SIGTERM, server.shutdown)
    signal.signal(signal.SIGINT, server.shutdown)
    signal.signal(signal.SIGBREAK, server.shutdown)

    server.run()

if __name__ == "__main__":
    main()
