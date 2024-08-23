from double_linked_list.DoubleLinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> DoubleLinkedList:
    return DoubleLinkedList()


@pytest.mark.double_linked_list
@pytest.mark.parametrize("items, expected_result",
                         [
                             ([1, 2, 3, 4], False),
                             ([1], False),
                             ([], True),
                         ])
def test_is_empty_positive(items, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    assert pre_condition.is_empty() == expected_result
