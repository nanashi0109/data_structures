from __future__ import annotations


class Deque:

    __head: Node
    __tail: Node

    class Node:

        next_node: Deque.Node
        prev_node: Deque.Node

        def __init__(self, data: any):
            self.data = data

    def __init__(self):
        self.__count = 0

    def enqueue_tail(self, item: any) -> None:
        node = Deque.Node(item)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.next_node = node
            node.prev_node = self.__tail

        self.__tail = node
        self.__count += 1

    def dequeue_head(self) -> Node:
        if self.is_empty():
            return None

        result = self.__head.data

        self.__head = self.__head.next_node
        self.__head.prev_node = None

        self.__count -= 1
        return result

    def peek_head(self) -> Node:
        return self.__head

    def enqueue_head(self, item: any) -> None:
        node = Deque.Node(item)

        if self.is_empty():
            self.__tail = node
        else:
            self.__head.prev_node = node
            node.next_node = self.__head

        self.__head = node
        self.__count += 1

    def dequeue_tail(self) -> Node:
        if self.is_empty():
            return None

        result = self.__tail.data

        self.__tail = self.__tail.prev_node
        self.__tail.next_node = None

        self.__count -= 1
        return result

    def peek_tail(self) -> Node:
        return self.__tail.data

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def get_count(self) -> int:
        return self.__count

    def __str__(self):
        result = "None <- (head) <- "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.data} <- "
            iterator = iterator.next_node

        result += "(tail) <- None\n"

        result += "None -> (tail) -> "

        iterator = self.__tail
        while not (iterator is None):
            result += f"{iterator.data} -> "
            iterator = iterator.prev_node

        result += "(head) -> None"

        return result
