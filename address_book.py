"""Homework 6: an address book built from classes.

Field is the base class for record fields; Name and Phone are fields;
Record keeps a name and a list of phones; AddressBook keeps records by name.
"""

from collections import UserDict

PHONE_LENGTH = 10


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Contact name, a required field."""

    def __init__(self, value):
        if not value:
            raise ValueError("Name is required.")
        super().__init__(value)


class Phone(Field):
    """Phone number of exactly 10 digits."""

    def __init__(self, value):
        if not (len(value) == PHONE_LENGTH and value.isdigit()):
            raise ValueError(f"Phone must contain exactly {PHONE_LENGTH} digits: {value!r}")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        found = self.find_phone(phone)
        if found is None:
            raise ValueError(f"Phone {phone} not found.")
        self.phones.remove(found)

    def edit_phone(self, old_phone, new_phone):
        found = self.find_phone(old_phone)
        if found is None:
            raise ValueError(f"Phone {old_phone} not found.")
        # Validate the new number before replacing the old one.
        self.phones[self.phones.index(found)] = Phone(new_phone)

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John's record to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print all records in the book
    for name, record in book.data.items():
        print(record)

    # Find and edit John's phone
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Contact name: John, phones: 1112223333; 5555555555

    # Find a specific phone in John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # John: 5555555555

    # Delete Jane's record
    book.delete("Jane")
