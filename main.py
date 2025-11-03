from src.repositories.contact_repository import ContactRepository
from src.services.contact_service import ContactService

CONTACT_JSON = 'data/contacts_json.json'
repository = ContactRepository(CONTACT_JSON)
service = ContactService(repository)


def print_contacts(contacts: list):
    if contacts:
        print('=' * 5 + "Контакты" + '=' * 5, '\n')
        for contact in contacts:
            print(contact.__str__())
            # print(f"ID: {contact.id}")
            # print(f"Имя: {contact.name}")
            # print(f"Номер телефона: {contact.phone}")
            # print(f"Почта: {contact.email}")
            print("-" * 30)
    else:
        print("Контактов нет")

def main():
    print('Добро пожаловать в контактную книгу!')

    while True:
        print('\n' + '=' * 30)
        print('1. Добавить контакт')
        print('2. Показать все контакты')
        print('3. Поиск контакта')
        print('4. Удалить контакт')
        print('5. Изменить контакт')
        print('6. Выйти')
        print('=' * 30)

        user_input = input('Выберите действие (1-6):')

        if user_input == '1':
            print("Введите данные для создания контакта:")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите Почту: ")
            service.add_contact(name, phone, email)
        elif user_input == '2':
            contacts = service.get_all_contacts()
            print_contacts(contacts)
        elif user_input == '3':
            user_search = input("Введите имя, номер телефона или почту контакта для поиска: ")
            found_contacts = service.search_contacts(user_search)
            print_contacts(found_contacts)
        elif user_input == '4':
            try:
                del_contact_id = int(input("Введите id контакта на удаление: "))
                print(service.search_contacts_by_id(del_contact_id))
                user_agree = input("Удалить данный контакт? Д/Н")
                if user_agree in ('Y', 'y', 'Д', 'д'):
                    try:
                        service.delete_contact(del_contact_id)
                        print("Контакт удалён")
                    except Exception as e:
                        print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Ошибка {e}")
        elif user_input == '5':
            print("Введите данные для изменения контакта:")
            id = int(input("Введите id: "))
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите Почту: ")
            service.update_contact(id, name, phone, email)
        elif user_input == '6':
            print("До свидания!")
            break
        else:
            print('\n' + "Выберите один из пунктов меню")


if __name__ == '__main__':
    main()
