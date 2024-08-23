from hash_table.HashTable import *
import pytest


@pytest.fixture(scope="function")
def pre_condition() -> HashTable:
    table = HashTable(500)

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
def test_get_positive(key, value, pre_condition):

    pre_condition.add(key, value)
    assert pre_condition.get(key) == value


@pytest.mark.hash_table
@pytest.mark.parametrize("key, value, key2, expected_result",
                         [
                             (32, 1, 12, pytest.raises(KeyError)),
                             (231, 3, 124, pytest.raises(KeyError)),
                             (31, 3, 134, pytest.raises(KeyError)),
                         ])
def test_get_negative(key, value, key2, expected_result, pre_condition):
    pre_condition.add(key, value)

    with expected_result:
        assert pre_condition.get(key2) == expected_result
