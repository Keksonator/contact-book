from src.repositories.contact_repository import ContactRepository
from src.services.contact_service import ContactService  # новый импорт!


def test_service():
    print("=== ТЕСТ СЕРВИСА ===")

    # Нанимаем всех сотрудников
    librarian = ContactRepository('contacts_json.json')
    consultant = ContactService(librarian)  # Консультанту даем Библиотекаря

    # Тест 1: Получить все контакты
    print("1. Получаем все контакты...")
    all_contacts = consultant.get_all_contacts()
    print(f"Контактов в базе: {len(all_contacts)}")

    # Тест 2: Добавить контакт
    print("2. Добавляем контакт через Консультанта...")
    new_id = consultant.add_contact("Анна Сервисова", "555-666", "anna@test.com")
    print(f"Добавлен контакт с ID: {new_id}")

    # Тест 3: Поиск
    print("3. Ищем 'Анна'...")
    found = consultant.search_contacts("Анна")
    print(f"Найдено: {len(found)} контактов")

    # Тест 4: Удаление
    print("4. Удаляем добавленный контакт...")
    success = consultant.delete_contact(new_id)
    print(f"Удаление успешно: {success}")

    print("=== ТЕСТ СЕРВИСА ЗАВЕРШЕН ===")