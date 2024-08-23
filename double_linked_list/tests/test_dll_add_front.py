from double_linked_list.DoubleLinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> DoubleLinkedList:
    return DoubleLinkedList()


@pytest.mark.double_linked_list
@pytest.mark.parametrize("item, expected_result",
                         [
                             (1, "None <- (tail) <-> 1 <-> (head) -> None"),
                             (4, "None <- (tail) <-> 4 <-> (head) -> None"),
                         ])
def test_add_front_positive_1(item, expected_result, pre_condition):
    pre_condition.add_front(item)
    assert str(pre_condition) == expected_result


@pytest.mark.double_linked_list
@pytest.mark.parametrize("items, expected_result",
                         [
                             ([1, 5, 2, 6, 2], "None <- (tail) <-> 1 <-> 5 <-> 2 <-> 6 <-> 2 <-> (head) -> None"),
                         ])
def test_add_front_positive_2(items, expected_result, pre_condition):
    for i in items:
        pre_condition.add_front(i)

    assert str(pre_condition) == expected_result
