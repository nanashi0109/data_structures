from __future__ import annotations


class Queue:
    class Node:

        next_node: Queue.Node or None

        def __init__(self, data: any):
            self.data = data
            self.prev_node = None

    __head: Node or None
    __tail: Node or None

    def __init__(self):
        self.__count = 0

        self.__head = None
        self.__tail = None

    def enqueue(self, item: any) -> None:
        node = Queue.Node(item)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev_node = node

        self.__tail = node
        self.__count += 1

    def dequeue(self) -> Node or None:
        if self.is_empty():
            return None

        result = self.__head.data

        if self.__count == 1:
            self.__tail = None

        self.__head = self.__head.prev_node

        self.__count -= 1
        return result

    def peek(self) -> Node or None:
        if self.is_empty():
            return None

        return self.__head.data

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def get_count(self) -> int:
        return self.__count

    def __str__(self):
        result = "(head) -> "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.data} -> "
            iterator = iterator.prev_node

        result += "(tail) -> None"

        return result
