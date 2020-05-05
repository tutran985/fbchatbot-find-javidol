import json

import requests


class JavIdol():
    def __init__(self):
        pass

    def look_up_actress(self, name=None):
        url = 'https://jav-rest-api-htpvmrzjet.now.sh/api/actress?name={}'.format(name)
        try:
            actressRequest = requests.get(url).json()
            mess = actressRequest['result']
        except:
            mess = 'Có thể bạn nhập bị sai :('

        return mess

    def look_up_movies(self, id=None):
        try:
            video_url = 'https://jav-rest-api-htpvmrzjet.now.sh/api/videos/'
            vidURL = video_url + id
            videoRequest = requests.get(vidURL).json()
            mess = videoRequest['result']
        except:
            mess = 'Có thể bạn nhập bị sai :('
        return mess