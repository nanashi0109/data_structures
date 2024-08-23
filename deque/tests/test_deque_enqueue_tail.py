from deque.Deque import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Deque:
    return Deque()


@pytest.mark.queue
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], "(head) -> 4 -> 3 -> 2 -> 1 -> (tail) -> None"),
                             ([1, True, 65], "(head) -> 1 -> True -> 65 -> (tail) -> None"),
                         ])
def test_enqueue_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue(i)

    assert str(pre_condition) == expected_result


@pytest.mark.queue
@pytest.mark.parametrize("start_queue, data, expected_result",
                         [
                             ([4, 3, 2, 1], 12, "(head) -> 4 -> 3 -> 2 -> 1 -> 12 -> (tail) -> None"),
                             ([1, 2, "65"], 76, "(head) -> 1 -> 2 -> 65 -> 76 -> (tail) -> None"),
                         ])
def test_enqueue_positive_2(start_queue, data, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue(i)

    pre_condition.enqueue(data)

    assert str(pre_condition) == expected_result
