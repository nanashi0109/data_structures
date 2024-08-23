from deque.Deque import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Deque:
    return Deque()


@pytest.mark.deque
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], 1),
                             ([1, 2, 65], 65),
                             ([], None),
                         ])
def test_dequeue_tail_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue_tail(i)

    assert pre_condition.dequeue_tail() == expected_result


@pytest.mark.deque
@pytest.mark.parametrize("start_queue, expected_result",
                         [
                             ([4, 3, 2, 1], "None <- (head) <-> 4 <-> 3 <-> 2 <-> (tail) -> None"),
                             ([1, 2, "65"], "None <- (head) <-> 1 <-> 2 <-> (tail) -> None"),
                         ])
def test_dequeue_tail_positive_2(start_queue, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue_tail(i)

    pre_condition.dequeue_tail()

    assert str(pre_condition) == expected_result
