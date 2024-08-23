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
                             ([], None),
                         ])
def test_pop_positive_1(data, expected_result, pre_condition):
    for i in data:
        pre_condition.push(i)

    assert pre_condition.pop() == expected_result


@pytest.mark.stack
@pytest.mark.parametrize("data, expected_result",
                         [
                             ([4, 3, 2, 1], "2 -> 3 -> 4 -> None"),
                             ([1, 2, 65], "2 -> 1 -> None"),
                             ([], "None"),
                         ])
def test_pop_positive_2(data, expected_result, pre_condition):
    for i in data:
        pre_condition.push(i)

    pre_condition.pop()
    assert str(pre_condition) == expected_result

