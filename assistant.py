from collections import UserDict

# Базовий клас для всіх полів, що зберігають значення
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені, наслідується від Field
class Name(Field):
    def __init__(self, value):
        self.value = value

# Клас для зберігання телефонного номера, наслідується від Field
class Phone(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # Перевірка, чи є значення телефонним номером з 10 цифр
        if self.value.isdigit() and len(self.value) == 10:
            return self.value

# Клас для зберігання запису, що містить ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ім'я запису
        self.phones = []  # Список телефонів

    # Додає телефон до запису
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Видаляє телефон з запису
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    # Знаходить телефон у записі
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    # Редагує існуючий телефон у записі
    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

    # Повертає рядкове представлення запису
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання адресної книги, наслідується від UserDict
class AddressBook(UserDict):
    # Додає запис до адресної книги
    def add_record(self, record):
        self.data[record.name.value] = record
    
    # Знаходить запис за ім'ям
    def find(self, name):
        return self.data.get(name, None)
    
    # Видаляє запис за ім'ям
    def delete(self, name):
        if name in self.data:
            del self.data[name]
