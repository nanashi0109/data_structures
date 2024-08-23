from __future__ import annotations


class HashTable:
    def __init__(self, size: int):
        self.__count = 0
        self.__size = size
        self.__array = [None] * self.__size

    def __hash(self, key: any) -> int:
        value = hash(key)
        return value % self.__size

    def add(self, key: any, item: any) -> None:
        if item is None:
            raise TypeError("Value of type None cannot be put in table ")

        _hash = self.__hash(key)
        if self.__array[_hash] is not None:
           raise KeyError("Collision")

        self.__array[_hash] = item
        self.__count += 1

    def get(self, key: any) -> any:
        _hash = self.__hash(key)

        item = self.__array[_hash]
        if item is None:
            raise KeyError("Key not found")

        return item

    def delete(self, key: any) -> None:
        _hash = self.__hash(key)

        if self.__array[_hash] is None:
            raise KeyError("Key not found")

        self.__array[_hash] = None
        self.__count -= 1
