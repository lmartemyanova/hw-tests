import pytest


def test_create_folder_positive(ya_auth):
    if ya_auth.check_path_exists('test'):
        pytest.skip('the folder already exists')
    response = ya_auth.create_folder('test')
    result = response.status_code
    expected = 201
    assert result == expected, 'the folder has not created'
    assert ya_auth.check_path_exists('test'), 'the folder has not found'


@pytest.mark.skip('the folder already exists')
def test_create_folder_exists(ya_auth):
    response = ya_auth.create_folder('test')
    result = response.status_code
    expected = 409
    assert result == expected, 'the folder already exists'


@pytest.mark.xfail
@pytest.mark.parametrize('error_code, res',
                         [(400, 'Некорректные данные.'),
                          (401, 'Не авторизован.'),
                          (403,
                           'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или '
                           'увеличьте объём Диска.'),
                          (404, 'Не удалось найти запрошенный ресурс.'),
                          (406, 'Ресурс не может быть представлен в запрошенном формате.'),
                          (413, 'Загрузка файла недоступна. Файл слишком большой.'),
                          (423, 'Технические работы. Сейчас можно только просматривать и скачивать файлы.'),
                          (429, 'Слишком много запросов.'),
                          (503, 'Сервис временно недоступен.'),
                          (507, 'Недостаточно свободного места.')]
                         )
def test_create_folder_with_errors(ya_auth, error_code, res):
    response = ya_auth.create_folder('test')
    result = response.status_code
    expected = error_code
    assert result == expected, res
