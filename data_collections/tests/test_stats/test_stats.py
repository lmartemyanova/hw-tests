import json

import pytest
from data_collections.stats import get_max_stats


def get_test_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


@pytest.mark.parametrize('test_data, expected',
                         zip(get_test_data('database/stats.json'),
                             ["yandex", "facebook", "ok"])
                         )
def test_get_max_stats(test_data, expected):
    result = get_max_stats(test_data)
    assert result == expected
