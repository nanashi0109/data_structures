from deque.Deque import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Deque:
    return Deque()


@pytest.mark.deque
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], 4),
                             (["1", 2, 65], "1"),
                             ([], None),
                         ])
def test_peek_head_positive(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue_tail(i)

    assert pre_condition.peek_head() == expected_result

