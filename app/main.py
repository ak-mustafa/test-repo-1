from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory phone book storage
phone_book: Dict[str, str] = {}

class Contact(BaseModel):
    name: str
    phone: str

@app.get("/contacts")
def get_contacts():
    """Retrieve all contacts."""
    return phone_book

@app.post("/contacts")
def add_contact(contact: Contact):
    """Add a new contact."""
    if contact.name in phone_book:
        return {"error": "Contact already exists."}
    phone_book[contact.name] = contact.phone
    return {"message": "Contact added successfully."}

@app.put("/contacts/{name}")
def update_contact(name: str, contact: Contact):
    """Update an existing contact."""
    if name not in phone_book:
        return {"error": "Contact not found."}
    phone_book[name] = contact.phone
    return {"message": "Contact updated successfully."}

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    """Delete a contact."""
    if name not in phone_book:
        return {"error": "Contact not found."}
    del phone_book[name]
    return {"message": "Contact deleted successfully."}