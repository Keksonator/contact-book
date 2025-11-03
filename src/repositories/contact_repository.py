import json

from src.models.contact import Contact


class ContactRepository:
    def __init__(self, filename):
        self.filename = filename

    def get_all(self) -> list[Contact]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

                contacts = []
                for contact_dict in data.get('contacts', []):
                    contact = Contact(
                        id=contact_dict['id'],
                        name=contact_dict['name'],
                        phone=contact_dict['phone'],
                        email=contact_dict['email']
                    )
                    contacts.append(contact)
                return contacts

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_all(self, contacts: list[Contact]):
        data = {'contacts': []}

        for contact in contacts:
            contact_data = {
                'id': contact.id,
                'name': contact.name,
                'phone': contact.phone,
                'email': contact.email
            }
            data['contacts'].append(contact_data)

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


