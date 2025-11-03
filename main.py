import json
from json import JSONDecodeError
from repositories import ContactRepository
from models import Contact

CONTACT_JSON = 'contacts_json.json'


class SimpleID:
    def __init__(self):
        self.current = 0

    def next(self):
        self.current += 1
        return self.current


# Глобальный генератор ID
id_generator = SimpleID()

def try_read_json(file_json):
    try:
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data and 'contacts' in data and data['contacts']:
                max_id = max(contact['id'] for contact in data['contacts'])
                id_generator.current = max_id
            return data
    except FileNotFoundError:
        print("Файл не найден")
        return {}
    except  JSONDecodeError:
        print("Невозможно прочитать файл")
        return {}


def save_json_data(data):
    with open(CONTACT_JSON, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def show_contacts(contacts):
    if not contacts:
        print("Список контактов пуст")
    else:
        value = contacts['contacts']
        print("--- Все контакты ---")
        print(value)


def add_contact(contacts):
    print("--- Добавление нового контакта ---")
    contact_name = input("Введите имя:")
    contact_phone = input("Введите телефон:")
    contact_email = input("Введите email:")

    new_id = id_generator.next()

    if contacts:
        contacts['contacts'].append(
            {
                'id': new_id,
                'name': contact_name,
                'phone': contact_phone,
                'email': contact_email
            }
        )
        return contacts
    else:
        contacts = {"contacts":
            [{
                'id': new_id,
                'name': contact_name,
                'phone': contact_phone,
                'email': contact_email}]
        }
        return contacts


def search_contacts(contacts):
    search_item = input('Введите имя, телефон или email для поиска:').strip().lower()

    if not search_item:
        print("Введите текст для поиска!")
        return

    found_contacts = []
    for contact_data in contacts["contacts"]:
        if search_item in contact_data["name"].strip().lower():
            found_contacts.append(contact_data)
            continue
        if search_item in contact_data["phone"].strip().lower():
            found_contacts.append(contact_data)
            continue
        if search_item in contact_data["email"].strip().lower():
            found_contacts.append(contact_data)
            continue

    if found_contacts:
        print(f"Найдено контактов:{len(found_contacts)}")

        print(found_contacts)
        return found_contacts

    else:
        print('Контакты не найдены.')


def del_contact(contacts: dict):
    if not contacts:
        print("Контактов для удаления нет!")
        return contacts

    show_contacts(contacts)
    try:
        user_chose = int(input("Введите id номер контакта на удаление: "))
    except Exception as e:
        print(f"{e}")
        print("Введите номер контакта!")
        return contacts
    for index, data in enumerate(contacts['contacts']):
        if user_chose == data['id']:
            try:
                contacts['contacts'].pop(index)
            except Exception as e:
                print(f"При удалении возникла ошибка: {e}")
            break
    print("Такого контакта нет")
    return contacts


def main():
    print('Добро пожаловать в контактную книгу!')
    contacts = try_read_json(CONTACT_JSON)

    while True:
        print('\n' + '=' * 30)
        print('1. Добавить контакт')
        print('2. Показать все контакты')
        print('3. Поиск контакта')
        print('4. Удалить контакт')
        print('5. Выйти')
        print('=' * 30)

        user_input = input('Выберите действие (1-5):')

        if user_input == '1':
            contacts = add_contact(contacts)
        elif user_input == '2':
            show_contacts(contacts)
        elif user_input == '3':
            search_contacts(contacts)
        elif user_input == '4':
            contacts = del_contact(contacts)
        elif user_input == '5':
            save_json_data(contacts)
            print("До свидания!")
            break
        else:
            print('\n' + "Выберите один из пунктов меню")


if __name__ == '__main__':
    main()
