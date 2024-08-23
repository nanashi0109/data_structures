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
@pytest.mark.parametrize("key, expected_result",
                         [
                             (1, pytest.raises(KeyError)),
                             (2, pytest.raises(KeyError)),
                             (3, pytest.raises(KeyError)),
                         ])
def test_delete(key, expected_result, pre_condition):
    pre_condition.delete(key)
    with expected_result:
       assert pre_condition.get(key) == expected_result

