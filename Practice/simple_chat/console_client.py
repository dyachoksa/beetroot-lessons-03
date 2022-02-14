import socket
import threading


class Client:
    def __init__(self, addr: str, port: int, name: str) -> None:
        self.addr = addr
        self.port = port
        self.name = name

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def run(self):
        self.client_socket.connect((self.addr, self.port))

        print("Successfully connected to {}:{}".format(self.addr, self.port))

        r_thread = threading.Thread(target=self.recieve_messages)
        r_thread.start()

        s_thread = threading.Thread(target=self.send_messages)
        s_thread.start()

        r_thread.join()
        s_thread.join()

    def recieve_messages(self):
        print("Starated 'recieve_messages' thread.")
        print("Thread id:", threading.get_native_id())

        while True:
            message = self.client_socket.recv(2048).decode("utf-8")

            if "[NAME]" in message:
                print(message.replace("[NAME]", ""))
                self.client_socket.send(self.name.encode("utf-8"))
                continue

            print(message)

    def send_messages(self):
        print("Starated 'send_messages' thread.")
        print("Thread id:", threading.get_native_id())

        while True:
            message = input("")
            self.client_socket.send(message.encode("utf-8"))


def main():
    addr = "127.0.0.1"
    port = 8899

    name = input("Your name: ")

    client = Client(addr, port, name)
    client.run()

if __name__ == "__main__":
    main()
