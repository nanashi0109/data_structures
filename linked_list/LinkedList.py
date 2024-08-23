from __future__ import annotations


class LinkedList:

    class Node:
        prev_node: LinkedList.Node or None

        def __init__(self, data: any):
            self.data = data
            self.prev_node = None

    __head: Node or None
    __tail: Node or None

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def add_front(self, item: any) -> None:
        node = LinkedList.Node(item)

        if not self.is_empty():
            node.prev_node = self.__head
        else:
            self.__tail = node

        self.__head = node
        self.__count += 1

    def add_back(self, item: any) -> None:
        node = LinkedList.Node(item)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev_node = node

        self.__tail = node
        self.__count += 1

    def remove(self, item: any) -> None:
        if self.is_empty():
            raise Exception("Not found")

        if self.__head.data is item:
            self.__head = self.__head.prev_node
        else:
            iterator = self.__head

            while not (iterator.prev_node.data is item):
                if iterator.prev_node.prev_node is None:
                    raise Exception("Not found")

                iterator = iterator.prev_node

            iterator.prev_node = iterator.prev_node.prev_node

        self.__count -= 1

    def insert(self, item: any, index: int) -> None:
        if self.__count - 1 < index or index < 0:
            raise ValueError("Incorrect index")

        if index == 0:
            self.add_front(item)
            return

        node = LinkedList.Node(item)

        node_iterator = self.__head
        counter = 0

        while counter < index - 1:
            node_iterator = node_iterator.prev_node
            counter += 1

        node.prev_node = node_iterator.prev_node
        node_iterator.prev_node = node

        self.__count += 1

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def find(self, item: any) -> bool:
        if self.is_empty():
            return False

        iterator = self.__head

        while not (iterator is None):
            if iterator.data is item:
                return True
            iterator = iterator.prev_node

        return False

    def count(self, item: any) -> int:
        if self.is_empty():
            return 0

        counter = 0
        iterator = self.__head

        while not (iterator is None):
            if iterator.data == item:
                counter += 1
            iterator = iterator.prev_node

        return counter

    def peek_front(self) -> any:
        return self.__head.data

    def peek_back(self) -> any:
        return self.__tail.data

    def clear(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    def __str__(self):
        result = "(head) -> "

        iterator = self.__head

        while not (iterator is None):
            result += f"{iterator.data} -> "
            iterator = iterator.prev_node

        result += "None"

        return result
