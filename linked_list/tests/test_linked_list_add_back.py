from linked_list.LinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> LinkedList:
    return LinkedList()


@pytest.mark.linked_list
@pytest.mark.parametrize("item, expected_result",
                         [
                             (1, "(head) -> 1 -> None"),
                             (4, "(head) -> 4 -> None"),
                         ])
def test_add_back_positive_1(item, expected_result, pre_condition):
    pre_condition.add_back(item)
    assert str(pre_condition) == expected_result


@pytest.mark.linked_list
@pytest.mark.parametrize("items, expected_result",
                         [
                             ([1, 5, 2, 6, 2], "(head) -> 1 -> 5 -> 2 -> 6 -> 2 -> None"),
                         ])
def test_add_back_positive_2(items, expected_result, pre_condition):
    for i in items:
        pre_condition.add_back(i)

    assert str(pre_condition) == expected_result
