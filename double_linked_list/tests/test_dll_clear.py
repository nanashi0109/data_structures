from double_linked_list.DoubleLinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> DoubleLinkedList:
    return DoubleLinkedList()


@pytest.mark.double_linked_list
@pytest.mark.parametrize("items",
                         [
                             ([1, 2, 3, 4]),
                             ([1, 2, 3, 4, 3, 2, 3, 4, 3]),
                             ([]),
                         ])
def test_clear_positive(items, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    pre_condition.clear()

    assert str(pre_condition) == "None <- (tail) <-> (head) -> None"
