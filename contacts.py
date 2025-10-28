

def show_contacts(contacts):
    if not contacts:
        print("Контактов пока нет!")
        return

    print("--- Все контакты ---")
    for contact_position, contact_data in enumerate(contacts, 1):
        print(f"{contact_position}. {contact_data['name']}")
        print(f"{' '*4}Телефон: {contact_data['phone']}")
        print(f"{' '*4}Email: {contact_data['email']}")
        print('-'*15)

def add_contact(contacts: list):
    print('--- Добавление нового контакта ---')
    contact_name = input("Введите имя:")
    contact_phone = input("Введите телефон:")
    contact_email = input("Введите email:")
    contacts.append(
        {
        'name': contact_name,
        'phone': contact_phone,
        'email':contact_email
         }
    )
    print(f"Контакт {contact_name} успешно добавлен!")
    return contacts


def search_contacts(contacts):
    if not contacts:
        print("Контактов для поиска нет!")
        return

    search_item = input('Введите имя, телефон или email для поиска:').strip().lower()

    if not search_item:
        print("Введите текст для поиска!")
        return

    found_contacts = []
    for contact_data in contacts:
        contact_value = [contact_val.lower() for contact_val in contact_data.values()]
        for i in contact_value:
            if search_item in i:
                found_contacts.append(contact_data)
                break

    if found_contacts:
        print(f"Найдено контактов:{len(found_contacts)}")
        show_contacts(found_contacts)

    else:
        print('Контакты не найдены.')

def del_contact(contacts: list):
    if not contacts:
        print("Контактов для удаления нет!")
        return contacts

    show_contacts(contacts)
    user_chose = input("Введите номер контакта на удаление:")

    if int(user_chose) in range(1, len(contacts)+1):

        user_arge = input("Подтвердите удаление контакта Д/Н : ").lower().strip()
        if user_arge == 'y' or user_arge == 'д':
            contacts.pop(int(user_chose)-1)
            print("Контакт успешно удалён")
            return contacts
        else:
            return
    else:
        print('Введите номер контакта!')
        return

def main():
    print('Добро пожаловать в контактную книгу!')
    contacts = []

    while True:
        print('\n'+'='*30)
        print('1. Добавить контакт')
        print('2. Показать все контакты')
        print('3. Поиск контакта')
        print('4. Удалить контакт')
        print('5. Выйти')
        print( '=' * 30 )

        user_input = input('Выберите действие (1-5):')

        if user_input == '1':
            add_contact(contacts)
        elif user_input == '2':
            show_contacts(contacts)
        elif user_input == '3':
            search_contacts(contacts)
        elif user_input == '4':
            del_contact(contacts)
        elif user_input == '5':
            print("До свидания!")
            break
        else:
            print('\n' + "Выберите один из пунктов меню")

if __name__=='__main__':
    main()