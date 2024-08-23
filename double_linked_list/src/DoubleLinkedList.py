from __future__ import annotations


class DoubleLinkedList:

    class Node:
        prev_node: DoubleLinkedList.Node or None
        next_node: DoubleLinkedList.Node or None

        def __init__(self, data: any):
            self.data = data
            self.prev_node = None
            self.next_node = None

    __head: Node or None
    __tail: Node or None

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def add_front(self, item: any) -> None:
        node = DoubleLinkedList.Node(item)

        if self.is_empty():
            self.__tail = node
        else:
            self.__head.next_node = node
            node.prev_node = self.__head

        self.__head = node
        self.__count += 1

    def add_back(self, item: any) -> None:
        node = DoubleLinkedList.Node(item)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev_node = node
            node.next_node = self.__tail

        self.__tail = node
        self.__count += 1

    def remove(self, item: any) -> None:
        if self.is_empty():
            raise Exception("Not found")

        iterator = self.__head
        while not (iterator.prev_node.data is item):
            if iterator.prev_node.prev_node is None:
                raise Exception("Not found")

            iterator = iterator.prev_node

        iterator.prev_node = iterator.prev_node.prev_node
        iterator.next_node = iterator
        self.__count -= 1

    def insert(self, item: any, index: int) -> None:
        if index > self.__count - 1 or index < 0:
            raise ValueError("Incorrect index")

        if index == 0:
            self.add_front(item)
            return

        node = DoubleLinkedList.Node(item)

        iterator = self.__head
        counter = 0

        while counter < index - 1:
            iterator = iterator.prev_node
            counter += 1

        node.prev_node = iterator.prev_node
        iterator.prev_node.next_node = node
        node.next_node = iterator
        iterator.prev_node = node

        self.__count += 1

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def find(self, item: any) -> bool:
        if self.is_empty():
            return False

        is_find = False
        iterator = self.__head

        while not is_find or iterator is not None:
            if iterator.data == item:
                is_find = True
            iterator = iterator.prev_node

        return is_find

    def count(self, item) -> int:
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
        result = "None <- (tail) <-> "

        iterator = self.__tail
        while not (iterator is None):
            result += f"{iterator.data} <-> "
            iterator = iterator.next_node

        result += "(head) -> None"

        return result

    def display_from_tail(self):
        result = "None <- (head) <- "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.data} <- "
            iterator = iterator.prev_node

        result += "(tail) <- None"

        print(result)

    def display_from_head(self):
        result = "None -> (tail) -> "

        iterator = self.__tail
        while not (iterator is None):
            result += f"{iterator.data} -> "
            iterator = iterator.next_node

        result += "(head) -> None"

        print(result)
