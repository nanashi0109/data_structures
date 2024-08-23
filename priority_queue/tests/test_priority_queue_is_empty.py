from priority_queue.PriorityQueue import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> PriorityQueue:
    return PriorityQueue()


@pytest.mark.priority_queue
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([[4, 1], [3, 3], [2, 1], [1, 0]], False),
                             ([["1", 2], [2, 3], [65, 1]], False),
                             ([], True),
                         ])
def test_is_empty_positive(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue(i[0], i[1])

    assert pre_condition.is_empty() == expected_result

