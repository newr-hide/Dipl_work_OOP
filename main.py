import requests
from pprint import pprint
import json
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
            'owner_id': '31616399', 'album_id': "profile", 'extended': 1
        }
        response = requests.get(url, params={**self.params, **params})
        return response.json()


access_token = 'vk1.a.dvYoKf9Kkke38EHfw1q1D1SyPlp6-EDrMwR41yLQ2ghnNj0VyPGmW-c9yQsjIdXKnAgTzWZLiV_gBKhLrp1LmlhBrIX8zBEl3eY4zr3ucyspCbJ3gnjCEf_QK9AG9uFlJ-TchYceU6txXbGUP9K_ecRHqPfOTpkgak-PU6lylYBpSQFTwz-ySbbsVL3cOXbd'
user_id = 'wwc21'
vk = VK(access_token, user_id)

tmp_vk = vk.photos_get()["response"]['items']

for i in tmp_vk:
    name_photo = i['likes']['count']
    for j in i['sizes']:
        if j['type'] == 'w':
            url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources/'
            params = {
                'path': 'Photo_VK'
            }
            headers = {
                'Authorization': 'OAuth y0_AgAAAAADBqHNAADLWwAAAAECiSyaAABbM4VSlj5OaZsg5MnbEw08iODqDg',
                'Accept': 'application/json', 'Content-Type': 'application/json'
            }

            response = requests.put(url_create_folder,
                                    params=params,
                                    headers=headers)

            # послать картинку на ЯД
            params = {
                'path': f'Photo_VK/{name_photo}',
                'url': j['url']
            }

            response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                     headers=headers,
                                     params=params)
            print(response.json())









# url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
# params = {
#     'path': 'Image_VK'
# }
# headers = {
#     'Authorization': 'OAuth y0_AgAAAAADBqHNAADLWwAAAAECiSyaAABbM4VSlj5OaZsg5MnbEw08iODqDg',
#     'Accept': 'application/json', 'Content-Type': 'application/json'
#            }
#
# response = requests.put(url_create_folder,
#                         params=params,
#                         headers=headers)
#
# # послать картинку на ЯД
# params = {
#     'path': 'Image_VK',
#     'url': tmp_lines
# }
#
# response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                         headers=headers,
#                         params=params)
# print(response.json())
# url_for_upload = response.json()['href']
#
# with open(image_name, 'rb') as f:
#     requests.put(url_for_upload,
#                  files={'file': f})
#     print(response)
