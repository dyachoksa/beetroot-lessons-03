import sqlite3


class ContactsService:
    def __init__(self, filename: str) -> None:
        self.filename = filename

        self.conn = sqlite3.connect(filename)

        self.init_db()

    def init_db(self):
        self.conn.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL,
    notes TEXT DEFAULT '- no notes -',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);        
        """)

    def get_contacts(self):
        rows = self.conn.execute("SELECT id, name, email, address, notes FROM contacts")

        return [{"id": row[0], "name": row[1], "email": row[2], "address": row[3], "notes": row[4]} for row in rows]

    def get_contact(self, contact_id):
        row = self.conn\
            .execute("SELECT id, name, email, address, notes FROM contacts WHERE id = ?", (contact_id,))\
            .fetchone()

        return {"id": row[0], "name": row[1], "email": row[2], "address": row[3], "notes": row[4]} \
            if row is not None \
            else None

    def create(self, contact):
        res = self.conn.execute(
            "INSERT INTO contacts (name, email, address, notes) VALUES (?, ?, ?, ?)",
            (contact["name"], contact["email"], contact["address"], contact["notes"])
        )
        self.conn.commit()

        contact_id = res.lastrowid

        contact["id"] = contact_id

        return contact_id

    def update(self, contact):
        self.conn.execute(
            "UPDATE contacts SET name = ?, email = ?, address = ?, notes = ? WHERE id = ?",
            (contact["name"], contact["email"], contact["address"], contact["notes"], contact["id"])
        )
        self.conn.commit()

    def delete(self, contact):
        self.conn.execute("DELETE FROM contacts WHERE id = ?", (contact["id"],))
        self.conn.commit()
