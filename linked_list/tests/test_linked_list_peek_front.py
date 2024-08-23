from linked_list.LinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> LinkedList:
    return LinkedList()


@pytest.mark.linked_list
@pytest.mark.parametrize("items, expected_result",
                         [
                             ([1, 2, 3, 4], 4),
                             ([1, 2, 3, 4, 3, 2, 3, 4, 3], 3),
                             ([1, False, True], True),
                         ])
def test_peek_front_positive(items, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    assert pre_condition.peek_front() == expected_result
