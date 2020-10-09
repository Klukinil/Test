import pytest

from dir_creator import YaUploader


def test_ya_folder():
    ya = YaUploader('newdir', '')
    assert ya.get_status() == 404
    assert ya.create_folder() == (201, 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Fnewdir')
    assert ya.get_status() == 200


def test_ya_folder_2():
    ya = YaUploader('newdir2', 'AgAAAAAcud6tAADLWzyhY5ZgpkX7lSqDp8GbPSE')
    assert ya.get_status() == 404
    assert ya.create_folder() == (201, 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Fnewdir2')
    assert ya.get_status() == 200


if __name__ == '__main__':
    pytest.main()