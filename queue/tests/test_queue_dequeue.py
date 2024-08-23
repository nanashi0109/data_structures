from queue.Queue import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Queue:
    return Queue()


@pytest.mark.queue
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], 4),
                             ([1, 2, 65], 1),
                             ([], None),
                         ])
def test_dequeue_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue(i)

    assert pre_condition.dequeue() == expected_result


@pytest.mark.queue
@pytest.mark.parametrize("start_queue, expected_result",
                         [
                             ([4, 3, 2, 1], "(head) -> 3 -> 2 -> 1 -> (tail) -> None"),
                             ([1, 2, "65"], "(head) -> 2 -> 65 -> (tail) -> None"),
                         ])
def test_dequeue_positive_2(start_queue, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue(i)

    pre_condition.dequeue()

    assert str(pre_condition) == expected_result
