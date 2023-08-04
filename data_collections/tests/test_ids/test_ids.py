import json

import pytest
from data_collections.ids import get_unique_ids


def get_test_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


@pytest.mark.parametrize('data, expected', zip(
    get_test_data('database/ids.json'),
    ([98, 35, 15, 213, 54, 119], [0, 2, 98, 745, 684459, 17, 637], [98, 589, 213, 758, 89])
))
def test_get_unique_ids(data, expected):
    result = get_unique_ids(data)
    assert result == expected
