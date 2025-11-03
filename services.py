from models import Contact
from repositories import ContactRepository


class ContactService:
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    def get_all_contacts(self):
        contacts = self.repository.get_all()
        return contacts

    def add_contact(self, name: str, phone: str, email: str) -> int:
        contacts = self.repository.get_all()

        if contacts:
            new_id = max(contact.id for contact in contacts) + 1
        else:
            new_id = 1

        new_contact = Contact(new_id, name, phone, email)

        contacts.append(new_contact)
        self.repository.save_all(contacts)

        return new_id

    def search_contacts(self, query: str) -> list[Contact]:
        contacts = self.repository.get_all()
        query = query.lower().strip()

        search_list = []
        if contacts:
            for contact in contacts:
                if (query in contact.email.lower() or
                        query in contact.name.lower() or
                        query in contact.phone.strip()):
                    search_list.append(contact)
            return search_list
        else:
            return []

    def search_contacts_by_id(self, user_id: int) -> Contact|None:
        contacts = self.repository.get_all()

        if contacts:
            for contact in contacts:
                if user_id == contact.id:
                    return contact
            return None
        else:
            return None

    def delete_contact(self, contact_id: int):
        contacts = self.repository.get_all()

        for index, contact in enumerate(contacts):
            if contact_id == contact.id:
                contacts.pop(index)
                self.repository.save_all(contacts)
                return True

        return False

    def update_contact(self, contact_id: int, name: str|None, phone: str|None, email: str|None ) -> Contact|None:
        contacts = self.repository.get_all()

        if not any([name, phone, email]):
            raise ValueError("Не указаны данные для обновления")

        for contact in contacts:
            if contact_id == contact.id:
                if name: contact.name = name
                if phone: contact.phone = phone
                if email: contact.email = email

                self.repository.save_all(contacts)
                return contact

        return None