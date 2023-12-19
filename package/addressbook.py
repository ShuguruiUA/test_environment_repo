import re
from collections import UserDict
from datetime import datetime
import pickle


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return str(self.value)


class Address(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value:
            self.__value = value.title()
        else:
            self.__value = None


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value:
            result = None
            get_email = re.findall(r'\b[a-zA-Z][\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', value)
            for i in get_email:
                result = i
            if result is None:
                raise AttributeError(f" Email is not correct {value}")
            self.__value = result
        else:
            self.__value = None





class Name(Field):
    pass


class Phone(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value: str):
        if len(new_value) == 10 and new_value.isdigit():
            self.__value = new_value
        else:
            raise ValueError("invalid phone number")

    def __str__(self):
        return self.value


class Birthday(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, date_birthday: str):
        if date_birthday:
            self.__value = date_birthday

    @classmethod
    def is_valid_value(cls, date_birthday):
        try:
            datetime.strptime(date_birthday, '%d-%m-%Y')
            return True
        except ValueError:
            return False


class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None):
        self.name = Name(name)
        if phone:
            self.phones = []
            self.phones.append(Phone(phone))
        else:
            self.phones = []
        self.birthday = Birthday(birthday)
        self.email = Email(email)
        self.address = Address(address)


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def add_email(self, email):
        self.email = Email(email)


    def add_address(self, address):
        self.address = Address(address)


    def add_birthday(self, birthday):
        if Birthday.is_valid_value(birthday):
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("format must be dd.mm.yyyy")


    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def remove_phone(self, phone_number):
        phone_object = self.find_phone(phone_number)
        if phone_object:
            self.phones.remove(phone_object)

    def edit_phone(self, phone_old_number, phone_new_number):
        phone_object = self.find_phone(phone_old_number)
        if phone_object:
            phone_object.value = phone_new_number
        else:
            raise ValueError

    def __str__(self):
        return (f"Contact name: {self.name.value}\n"
                f"Phones: {'; '.join(p.value for p in self.phones)}\n"
                f"Birthday: {self.birthday.value if self.birthday else 'no'}\n"
                f"Email: {self.email.value if self.email else 'no'}\n"
                f"Address: {self.address.value if self.address else 'no'}\n")


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.file_name = "addressBook.bin"

    def iterator(self, n: int = 2):
        result = f"{'-' * 50}\n"
        count = 0
        id_ = 0
        for name, record in self.data.items():
            result += f"{id_}: {record}\n"
            id_ += 1
            count += 1
            if count >= n:
                yield result
                count = 0
                result = f"{'-' * 50}\n"
        yield result

    def add_record(self, record_: Record):
        self.data[record_.name.value] = record_

    def find(self, name_):
        return self.data.get(name_)

    def delete(self, name_):
        record_book = self.find(name_)
        if record_book:
            del self.data[name_]

    def saved_to_file(self):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.data, fh)
            print(type(fh))

    def load_from_file(self):
        try:
            with open(self.file_name, "rb") as fh:
                self.data = pickle.load(fh)
        except FileNotFoundError:
            print("File not found")

    def search_informathion(self, info: str) -> str:
        correct_info = ""
        for name_, record_ in self.data.items():
            if info.lower() in name_.lower():
                correct_info += str(record_) + "\n"
            else:
                for phone in record_.phones:
                    if info.lower() in phone.value.lower():
                        correct_info += str(record_) + "\n"
                        break
        return correct_info


if __name__ == "__main__":
    book = AddressBook()
    #book.load_from_file()
    # book.search_informathion("T")
    #info_data = book.search_informathion("T")
    # for name_, record_ in info_data.items:
    #     print(record_)
    tom = Record("Tom","1234567890", "25-05-1992", "tom@gmail.com", "Kherson")
    print(tom)
    nick = Record("Nick")
    nick.add_phone("0987654321")
    print(nick.phones[0].value)
    nick.add_birthday("30-05-1991")
    print(nick.birthday.value)
    print(nick.email.value)
    nick.add_email("nick@gmail.com")
    nick.add_address("Odessa")
    print(nick)