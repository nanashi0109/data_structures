from double_linked_list.DoubleLinkedList import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> DoubleLinkedList:
    return DoubleLinkedList()


@pytest.mark.double_linked_list
@pytest.mark.parametrize("items, remove_item, expected_result",
                         [
                             ([1, 5, 2, 6, 2], 2, "None <- (tail) <-> 2 <-> 6 <-> 5 <-> 1 <-> (head) -> None"),
                             ([1, 5, 2, False, 2], False, "None <- (tail) <-> 2 <-> 2 <-> 5 <-> 1 <-> (head) -> None"),
                             ([1, 5, 2, 6, 2], 1, "None <- (tail) <-> 2 <-> 6 <-> 2 <-> 5 <-> (head) -> None"),
                         ])
def test_remove_positive(items, remove_item, expected_result, pre_condition):
    for i in items:
        pre_condition.add_back(i)

    pre_condition.remove(remove_item)
    assert str(pre_condition) == expected_result


@pytest.mark.double_linked_list
@pytest.mark.parametrize("items, remove_item, expected_result",
                         [
                             ([1, 5, 2, 6, 2], 0, pytest.raises(Exception)),
                             ([1, 5, 2, 6, 2], False, pytest.raises(Exception)),
                         ])
def test_remove_negative(items, remove_item, expected_result, pre_condition):
    for i in items:
        pre_condition.add_back(i)
    with expected_result:
        assert pre_condition.remove(remove_item) == expected_result

