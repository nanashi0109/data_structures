from deque.Deque import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Deque:
    return Deque()


@pytest.mark.deque
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], False),
                             (["1"], False),
                             ([], True),
                         ])
def test_is_empty_positive(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue_tail(i)

    assert pre_condition.is_empty() == expected_result

