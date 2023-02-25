from collections import UserDict, UserList, UserString


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record(Name, Phone):

    def __init__(self, name, phone):
        self.name = name
        self.phones = []
        self.phones.append(phone)

    def add_contacts(self, dictionary={}):
        self.dictionary = dictionary
        a = ({name: self.phones})
        self.dictionary.update(a)
        return (self.dictionary)

    def remove_contacts(self, name, dictionary={}):
        self.name = name
        a = dictionary.pop(name)
        return (dictionary)


class AddressBook(UserDict, Record):

    def add_record(self, rec):

        self.data[rec.name.value] = rec
        return self.data


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')
