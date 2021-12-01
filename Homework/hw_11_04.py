import datetime as dt

class CustomExeption(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        # write message to the file
        with open("logs.txt", "a") as f:
            f.write(f"[{dt.datetime.now()}]: {msg}\n")


raise CustomExeption("It's a custom exception time")
