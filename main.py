import requests
from datetime import datetime as dt
import time
from tqdm import tqdm

def copy_photo_from_VK_in_YaD(VK_id, access_token_VK, token_YAD, album="profile" ):


    class VK:
        def __init__(self, access_token, user_id, version='5.131'):
            self.token = access_token
            self.id = user_id
            self.version = version
            self.params = {'access_token': self.token, 'v': self.version}

        def users_info(self):
            url = 'https://api.vk.com/method/users.get'
            params = {'user_ids': self.id}
            response = requests.get(url, params={**self.params, **params})
            return response.json()

        def photos_get(self):
            url = 'https://api.vk.com/method/photos.get'
            params = {
                'owner_id': '31616399', 'album_id': album, 'extended': 1
            }
            response = requests.get(url, params={**self.params, **params})
            return response.json()


    access_token = access_token_VK
    user_id = VK_id
    vk = VK(access_token, user_id)
    print(vk.photos_get())
    tmp_vk = vk.photos_get()["response"]['items']

    def _add_date_to_file_name(file_name):
        date_str = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        new_file_name = str(file_name) + '_' + str(date_str)
        return new_file_name


    tmp_name = ''


    for i in tqdm(tmp_vk):

        name_photo = i['likes']['count']
        for j in i['sizes']:
            if j['type'] == 'w':
                url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources/'
                params = {
                    'path': 'Photo_VK'
                }
                headers = {
                    'Authorization': token_YAD,
                    'Accept': 'application/json', 'Content-Type': 'application/json'
                }

                response = requests.put(url_create_folder,
                                        params=params,
                                        headers=headers)
                if name_photo == tmp_name:

                    params = {
                        'path': f'Photo_VK/{_add_date_to_file_name(name_photo)}',
                        'url': j['url']
                    }
                else:
                    params = {
                        'path': f'Photo_VK/{name_photo}',
                        'url': j['url']
                    }

                tmp_name = name_photo
                response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                        headers=headers,
                                        params=params)
                time.sleep(1)
                print(response.json())


