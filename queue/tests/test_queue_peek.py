from queue.Queue import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Queue:
    return Queue()


@pytest.mark.queue
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], 4),
                             (["1", 2, 65], "1"),
                             ([], None),
                         ])
def test_peek_positive(data, expected_result, pre_condition):
    for i in data:
        pre_condition.enqueue(i)

    assert pre_condition.peek() == expected_result

