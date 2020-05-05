import json

import requests


class Simi():
    def __init__(self):
        pass

    def simi(self, maxii=None):
        url = 'https://wsapi.simsimi.com/190410/talk'
        headers = {
            'x-api-key': 'DudxAElQek6RUPZHvkEQaTP0ozigj3ihV3MiXO.R',
            'Content-Type': 'application/json',

        }
        data = {
            "utext": "{}".format(maxii),
            "lang": "vi"
        }
        try:
            r = requests.post(url, headers=headers, data=json.dumps(data))
            response = r.json()
            mess = response['atext']
        except:
            mess = 'Có thể con giáp bạn nhập bị sai :('

        return mess

# a = Simi().simi("s")