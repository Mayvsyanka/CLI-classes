from collections import UserDict


class Name:
    def __init__(self, name=None):
        self.name = name


class Phone:
    def __init__(self, phone=None):
        self.phone = phone


class Record:

    def add_contacts(self, name, phone, dictionary={}):
        self.name = name
        self.phone = phone
        a = ({self.name: self.phone})
        dictionary.update(a)
        return (dictionary)

    def change_contacts(self, name, phone, dictionary={}):
        self.name = name
        self.phone = phone
        dictionary[name] = phone
        return (dictionary)

    def remove_contacts(self, name, dictionary={}):
        self.name = name
        a = dictionary.pop(name)
        return (dictionary)


class AddressBook(UserDict, Record):
    def datadict(self):
        return (self.data)

    def add_record(self):
        rec = Record()
        dictionary = self.data
        if name.name in dictionary:
            rec.add_contacts(name.name, phone.phone, dictionary)
        else:
            rec.change_contacts(name.name, phone.phone, dictionary)
        return (self.data)


if __name__ == '__main__':
    ab = AddressBook({"Bill": "098908", "Mary": "20202"})
    name = Name('Bill')
    phone = Phone('123456')
    print(ab.add_record())
