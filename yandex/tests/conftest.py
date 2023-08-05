import os

import pytest
from dotenv import load_dotenv, find_dotenv

from yandex.yandex import YandexDisk


@pytest.fixture(scope='session')
def ya_auth():
    load_dotenv(find_dotenv())
    ya_uploader = YandexDisk(token=os.getenv('ya_token'))
    return ya_uploader
