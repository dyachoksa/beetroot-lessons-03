import typing


class Database:
    def __init__(self, uri: str) -> None:
        self.uri = uri
        self.openned = False

    def __enter__(self) -> "Database":
        self.open()

        return self

    def __exit__(self, exc_type, exc_value, traceback) -> typing.Literal[False]:
        self.close()

        # print(exc_type)
        # print(exc_value)

        return False

    def open(self) -> bool:
        print("Opennig database connection to {}...".format(self.uri))
        self.openned = True

        return True
    
    def close(self):
        print("Closing database connection...")
        self.openned = False

    def query(self, query: str):
        if not self.openned:
            raise RuntimeError("Database not connected")

        print("Executing query: {}".format(query))


# # Create instance of Database
# db = Database("postgresql://localhost/app")

# # Open connection to database
# if db.open():
#     print("Database connected")

# # Do some queries
# db.query("selecting users")
# db.query("selecting products")

# # Close connection to database
# db.close()

with Database("postgresql://localhost/app") as db:
    db.query("selecting users")
    db.query("selecting products")
