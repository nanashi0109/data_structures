from stack.Stack import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Stack:
    return Stack()


@pytest.mark.stack
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], 1),
                             ([1, 2, 65], 65),
                             ([1, 2, "65"], "65"),
                         ])
def test_peek_positive(data, expected_result, pre_condition):
    for i in data:
        pre_condition.push(i)

    assert pre_condition.peek() == expected_result

