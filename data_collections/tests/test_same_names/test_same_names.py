import json

import pytest
from data_collections.same_names import find_same_names


def get_test_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


@pytest.mark.parametrize('test_data, expected',
                         zip(get_test_data('database/courses_info.json'),
                             get_test_data('tests/expected_results/names_expected.json')))
def test_find_same_names(test_data, expected):
    result = find_same_names(test_data)
    assert result == expected
