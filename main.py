import requests


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

access_token = 'vk1.a.6PQPieXXl_a-fLVAvvP-KPsT492K6jXY2C9LEzmSv6NE7fcYKOstZKXKkaLDPQJdW7ReF57zqduCvPgf6IntEnp90aVwmzjvcypVo7sxZdgOcAQj4cKqQQiZqFKSlk9RleOj-iUvy5Dc8pKtn_FaUTsRQjVhffbNizatpcVrxHlOH_VwG4uP8adCfolX2QQt'
user_id = 'wwc21'
vk = VK(access_token, user_id)

print(vk.users_info())
# токен полученный из инструкции
