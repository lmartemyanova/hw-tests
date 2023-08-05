import requests


class YandexDisk:
    """
    Class YandexDisk for uploading files to user's Yandex Disk

    attribute 'url': for requests to REST API Yandex Disk

    """

    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token: str):
        """
        To initial the class YandexDisk object

        :param token (str): OAuth token of user's YandexDisk (collected by user input)

        """

        self.token = token

    def get_headers(self):
        """
        Method of getting headers for requests

        :return headers (dict)

        """

        headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        return headers

    def create_folder(self, folder_name):
        """
        Method allows to create a folder in user's Yandex Disk files

        :return response

        """

        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.put(self.url, headers=headers, params=params)
        return response

    def check_path_exists(self, path):
        """
        Method allows to check if path exists
        :param path: path (folder or file name)
        :return: bool (True if exists else False)
        """

        headers = self.get_headers()
        params = {'path': f'disk:/{path}'}
        response = requests.get(self.url, headers=headers, params=params)
        if response.status_code == 200:
            return True
        return False
