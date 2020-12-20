import requests

URL = "https://cloud-api.yandex.net/v1/disk/resources"
token = ''
headers = {"Authorization": f"OAuth {token}"}


def ya_disk_status_info(path):
    params = {'path': path}
    r = requests.get(url=URL, params=params, headers=headers)
    return r.status_code


def get_new_folder(folder_name, token):
    params = {'path': folder_name}
    r = requests.put(url=URL, params=params, headers={"Authorization": f"OAuth {token}"})
    return r.status_code


def delete_new_folder(folder_name):
    params = {'path': folder_name, 'permanently': True}
    r = requests.delete(url=URL, params=params, headers=headers)
    return r.status_code


if __name__ == '__main__':
    ya_disk_status_info('disk:/')
    get_new_folder('Media', '')
    delete_new_folder('Media')
