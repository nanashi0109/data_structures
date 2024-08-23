from hash_table.HashTable import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> HashTable:
    table = HashTable(100)

    table.add(1, 1)
    table.add(2, 2)
    table.add(3, 3)

    return table


@pytest.mark.hash_table
@pytest.mark.parametrize("key, value",
                         [
                             (False, 1),
                             ("1", 1),
                             (5, 1),
                         ])
def test_add_positive(key, value, pre_condition):

    pre_condition.add(key, value)
    assert pre_condition.get(key) == value


@pytest.mark.hash_table
@pytest.mark.parametrize("key, value, expected_result",
                         [
                             (1, 1, pytest.raises(KeyError)),
                             (2, False, pytest.raises(KeyError)),
                             (3, True, pytest.raises(KeyError)),
                         ])
def test_add_negative(key, value, expected_result, pre_condition):
    with expected_result:
        assert pre_condition.add(key, value) == expected_result
