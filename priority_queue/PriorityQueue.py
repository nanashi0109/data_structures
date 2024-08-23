from __future__ import annotations


class PriorityQueue:
    class Node:

        next_node: PriorityQueue.Node or None

        def __init__(self, data: any, priority: int):
            self.data = data
            self.next_node = None
            self.priority = priority

    __head: Node or None
    __tail: Node or None

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, item: any, priority: int) -> None:
        node = PriorityQueue.Node(item, priority)

        if self.is_empty():
            self.__tail = node
            self.__head = node

        elif self.__tail.priority <= node.priority:
            self.__tail.next_node = node
            self.__tail = node
        elif self.__head.priority > node.priority:
            node.next_node = self.__head
            self.__head = node
        else:
            iterator = self.__head
            while iterator.next_node.priority < node.priority:
                iterator = iterator.next_node

            node.next_node = iterator.next_node
            iterator.next_node = node

        self.__count += 1

    def dequeue(self) -> any:
        if self.is_empty():
            return None

        result = self.__head.data

        self.__head = self.__head.next_node
        self.__count -= 1
        return result

    def peek(self) -> Node or None:
        if self.is_empty():
            return None
        return self.__head.data

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def __str__(self):
        result = "(head) -> "

        iterator = self.__head
        while not (iterator is None):
            result += f"({iterator.data} : {iterator.priority}) -> "
            iterator = iterator.next_node
        result += "(tail) -> None"
        return result
