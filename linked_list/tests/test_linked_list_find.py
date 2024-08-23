from linked_list.LinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> LinkedList:
    return LinkedList()


@pytest.mark.linked_list
@pytest.mark.parametrize("items, find_item, expected_result",
                         [
                             ([1, 2, 3, 4], 1, True),
                             ([1, 2, 3, 4], 5, False),
                             ([1, False, True, 4], False, True),
                         ])
def test_find_positive(items, find_item, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    assert pre_condition.find(find_item) == expected_result
