import requests as r
import os


class YaUploader:
    def __init__(self, dir_name, token):
        self.dir_name = dir_name
        self.token = token

    def get_status(self):

        return r.get(f"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{self.dir_name}",
        headers = {'Authorization': self.token}).status_code

    def create_folder(self):
        put = r.put(f"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{self.dir_name}",
        headers = {'Authorization': self.token})
        try:
            return put.status_code, put.json()["message"]
        except KeyError:
            return put.status_code, put.json()["href"]


if __name__ == '__main__':
    ya_1 = YaUploader('newdir', '')
    print(ya_1.get_status())
    print(ya_1.create_folder())