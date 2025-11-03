from repositories import ContactRepository
from models import Contact

def test_repository():
    print("=== ТЕСТ БИБЛИОТЕКАРЯ ===")

    # Создаем библиотекаря
    repo = ContactRepository('contacts_json.json')

    # Тест 1: Чтение существующих контактов
    print("1. Читаем контакты с полки...")
    contacts = repo.get_all()
    print(f"Нашлось контактов: {len(contacts)}")
    for contact in contacts:
        print(f"   - {contact.name}")

    # Тест 2: Добавляем новый контакт
    print("2. Добавляем тестовый контакт...")
    new_contact = Contact(999, "Тест Иванов", "111-222", "test@test.ru")
    contacts.append(new_contact)

    # Сохраняем обратно
    repo.save_all(contacts)
    print("Сохранено!")

    # Тест 3: Проверяем, что сохранилось
    print("3. Проверяем сохранение...")
    updated_contacts = repo.get_all()
    print(f"Теперь контактов: {len(updated_contacts)}")

    print("=== ТЕСТ ЗАВЕРШЕН ===")


