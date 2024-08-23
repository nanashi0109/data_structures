from linked_list.LinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> LinkedList:
    return LinkedList()


@pytest.mark.linked_list
@pytest.mark.parametrize("items, item, index, expected_result",
                         [
                             ([1, 5, 2, 6, 2], 1, 0, "(head) -> 1 -> 2 -> 6 -> 2 -> 5 -> 1 -> None"),
                             ([1, 5, 2, 6, 2], 3, 3, "(head) -> 2 -> 6 -> 2 -> 3 -> 5 -> 1 -> None"),
                         ])
def test_insert_positive(items, item, index, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    pre_condition.insert(item, index)

    assert str(pre_condition) == expected_result


@pytest.mark.linked_list
@pytest.mark.parametrize("items, item, index, expected_result",
                         [
                             ([1, 5, 2], 4, 10, pytest.raises(ValueError)),
                             ([12], 4, -1, pytest.raises(ValueError)),
                         ])
def test_insert_negative(items, item, index, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    with expected_result:
        assert pre_condition.insert(item, index) == expected_result

