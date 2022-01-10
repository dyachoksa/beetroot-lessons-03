import json
import uuid

from PyQt6.sip import delete


class ContactsService:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.contacts = []

        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.contacts = json.load(f)
        except:
            self.contacts = []
    
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def get_contacts(self):
        return self.contacts

    def get_contact(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                return contact
        
        return None

    def create(self, contact):
        contact["id"] = str(uuid.uuid4())
        self.contacts.append(contact)

        self.save()

    def update(self, contact):
        for contact_to_update in self.contacts:
            if contact_to_update["id"] == contact["id"]:
                contact_to_update["name"] = contact["name"]
                contact_to_update["email"] = contact["email"]
                contact_to_update["address"] = contact["address"]
                contact_to_update["notes"] = contact["notes"]
        
        self.save()
    
    def delete(self, contact):
        self.contacts.remove(contact)
        self.save()
