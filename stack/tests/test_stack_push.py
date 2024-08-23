from stack.Stack import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> Stack:
    return Stack()


@pytest.mark.stack
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], "1 -> 2 -> 3 -> 4 -> None"),
                             ([1, 2, 65], "65 -> 2 -> 1 -> None"),
                         ])
def test_push_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.push(i)

    assert str(pre_condition) == expected_result


@pytest.mark.stack
@pytest.mark.parametrize("start_stack, data, expected_result",
                         [
                             ([4, 3, 2, 1], 12, "12 -> 1 -> 2 -> 3 -> 4 -> None"),
                             ([1, 2, "65"], 76, "76 -> 65 -> 2 -> 1 -> None"),
                         ])
def test_push_positive_2(start_stack, data, expected_result, pre_condition):
    for i in start_stack:
        pre_condition.push(i)

    pre_condition.push(data)

    assert str(pre_condition) == expected_result
