from deque.Deque import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Deque:
    return Deque()


@pytest.mark.deque
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], 4),
                             ([1, 2, 65], 1),
                             ([], None),
                         ])
def test_dequeue_head_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue_tail(i)

    assert pre_condition.dequeue_head() == expected_result


@pytest.mark.deque
@pytest.mark.parametrize("start_queue, expected_result",
                         [
                             ([4, 3, 2, 1], "None <- (head) <-> 3 <-> 2 <-> 1 <-> (tail) -> None"),
                             ([1, 2, "65"], "None <- (head) <-> 2 <-> 65 <-> (tail) -> None"),
                         ])
def test_dequeue_head_positive_2(start_queue, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue_tail(i)

    pre_condition.dequeue_head()

    assert str(pre_condition) == expected_result
