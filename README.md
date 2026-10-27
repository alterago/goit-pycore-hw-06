# goit-pycore-hw-06

Homework for topic 9 of the course "Python Programming: Foundations and Best Practices 2.0": basics of classes.

`address_book.py` implements an address book:

- `Field` — base class for record fields;
- `Name` — contact name (required);
- `Phone` — phone number with validation (exactly 10 digits);
- `Record` — a contact: name and a list of phones; `add_phone`, `remove_phone`, `edit_phone`, `find_phone`;
- `AddressBook` (a `UserDict`) — records by name; `add_record`, `find`, `delete`.

Run the usage example from the task:

```bash
python address_book.py
```
