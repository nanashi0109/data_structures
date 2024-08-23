from deque.Deque import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Deque:
    return Deque()


@pytest.mark.deque
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], "None <- (head) <-> 1 <-> 2 <-> 3 <-> 4 <-> (tail) -> None"),
                             ([1, True, 65], "None <- (head) <-> 65 <-> True <-> 1 <-> (tail) -> None"),
                         ])
def test_enqueue_head_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue_head(i)

    assert str(pre_condition) == expected_result


@pytest.mark.deque
@pytest.mark.parametrize("start_queue, data, expected_result",
                         [
                             ([4, 3, 2, 1], 12, "None <- (head) <-> 12 <-> 1 <-> 2 <-> 3 <-> 4 <-> (tail) -> None"),
                             ([1, 2, "65"], 76, "None <- (head) <-> 76 <-> 65 <-> 2 <-> 1 <-> (tail) -> None"),
                         ])
def test_enqueue_head_positive_2(start_queue, data, expected_result, pre_condition):
    for i in start_queue:
        pre_condition.enqueue_head(i)

    pre_condition.enqueue_head(data)

    assert str(pre_condition) == expected_result
