class Database:
    def __init__(self, uri: str) -> None:
        self.uri = uri
        self.openned = False

    def __enter__(self):
        self.open()

        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.close()

        # print(exc_type)
        # print(exc_value)

        return False

    def open(self):
        print("Opennig database connection to {}...".format(self.uri))
        self.openned = True
    
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
# db.open()

# # Do some queries
# db.query("selecting users")
# db.query("selecting products")

# # Close connection to database
# db.close()

with Database("postgresql://localhost/app") as db:
    db.query("selecting users")
    db.query("selecting products")
