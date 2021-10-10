from typing import  List


class User(object):
    __slots__ = ['name', 'surname', 'dob', 'addresses']

    def __init__(self, name: str, surname: str, dob: int, addresses: List):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.addresses = addresses

    def add_address(self, adr):
        self.addresses.append(adr)

    def remove_addr(self, index):
        if index < len(self.addresses):
            self.addresses.pop(index)
