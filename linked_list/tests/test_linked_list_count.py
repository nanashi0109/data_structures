from linked_list.LinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> LinkedList:
    return LinkedList()


@pytest.mark.linked_list
@pytest.mark.parametrize("items, find_item, expected_result",
                         [
                             ([1, 2, 3, 4], 1, 1),
                             ([1, 2, 3, 4, 3, 2, 3, 4, 3], 3, 4),
                             ([1, False, True, 4], False, 1),
                             ([1, 2, 1, 4], 5, 0),
                         ])
def test_count_positive(items, find_item, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    assert pre_condition.count(find_item) == expected_result
