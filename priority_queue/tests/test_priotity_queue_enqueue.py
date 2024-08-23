from priority_queue.PriorityQueue import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> PriorityQueue:
    return PriorityQueue()


@pytest.mark.priority_queue
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([[4, 4], [3, 2], [2, 5], [1, 2]], "(head) -> (3 : 2) -> (1 : 2) -> (4 : 4) -> (2 : 5) -> (tail) -> None"),
                             ([[1, 3], [True, 3], [65, 1]], "(head) -> (65 : 1) -> (1 : 3) -> (True : 3) -> (tail) -> None"),
                         ])
def test_enqueue_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue(i[0], i[1])

    assert str(pre_condition) == expected_result


@pytest.mark.priority_queue
@pytest.mark.parametrize("start_queue, data, expected_result",
                         [
                             ([[4, 2], [3, 3], [2, 2], [1, 3]], [12, 1], "(head) -> (12 : 1) -> (4 : 2) -> (2 : 2) -> (3 : 3) -> (1 : 3) -> (tail) -> None"),
                             ([[1, 2], [2, 2], ["65", 1]], [76, 2], "(head) -> (65 : 1) -> (1 : 2) -> (2 : 2) -> (76 : 2) -> (tail) -> None"),
                         ])
def test_enqueue_positive_2(start_queue, data, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue(i[0], i[1])

    pre_condition.enqueue(data[0], data[1])

    assert str(pre_condition) == expected_result
