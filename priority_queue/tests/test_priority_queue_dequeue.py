from priority_queue.PriorityQueue import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> PriorityQueue:
    return PriorityQueue()


@pytest.mark.priority_queue
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([[4, 4], [3, 2], [2, 5], [1, 2]], 3),
                             ([[1, 3], [True, 1], [65, 2]], True),
                             ([], None),
                         ])
def test_dequeue_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue(i[0], i[1])

    assert pre_condition.dequeue() == expected_result


@pytest.mark.priority_queue
@pytest.mark.parametrize("start_queue, expected_result",
                         [
                             ([[4, 2], [3, 3], [2, 2], [1, 3], [12, 1]], "(head) -> (4 : 2) -> (2 : 2) -> (3 : 3) -> (1 : 3) -> (tail) -> None"),
                             ([[1, 2], [2, 2], ["65", 1], [76, 2]], "(head) -> (1 : 2) -> (2 : 2) -> (76 : 2) -> (tail) -> None"),
                         ])
def test_dequeue_positive_2(start_queue, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue(i[0], i[1])

    pre_condition.dequeue()

    assert str(pre_condition) == expected_result
