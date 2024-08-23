from linked_list.LinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> LinkedList:
    return LinkedList()


@pytest.mark.linked_list
@pytest.mark.parametrize("items, expected_result",
                         [
                             ([1, 2, 3, 4], 1),
                             ([1, 2, 3, 4, 3, 2, 3, 4, 3], 1),
                             ([1, False, True], 1),
                         ])
def test_peek_back_positive(items, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    assert pre_condition.peek_back() == expected_result
