
class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(id={self.id}, name='{self.name}', phone='{self.phone}', email='{self.email}')"

    def __str__(self):
        return (f"Контакт: \n"
                f"Имя:{self.name} \n"
                f"Телефон:{self.phone}\n"
                f"Почта: {self.email}\n"
                f"ID: {self.id}\n")

