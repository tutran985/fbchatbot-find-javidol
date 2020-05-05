# -*- coding: utf-8 -*-
import json

from fbchat import log, Client
from fbchat.models import *
from bot_simi import Simi
from javidol import JavIdol


class AutoBot(Client):
    ass = 0
    idol_seach = 0
    movies_seach = 0

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info('Đã nhận được tin nhắn từ {} với nội dung là: {}'.format(author_id, message_object))

        if author_id != self.uid:
            if message_object.text:
                if message_object.text == '/Getid' or message_object.text == '/getid':
                    self.send(Message(text=message_object.author), thread_id=thread_id, thread_type=thread_type)

                elif '/simi' in message_object.text:
                    self.ass += 2
                    self.send(Message(text="Hi i'm simsimi"), thread_id=thread_id, thread_type=thread_type)
                elif self.ass > 1 and message_object.text:
                    mess = message_object.text
                    simmi = Simi()
                    simi_text = simmi.simi(maxii=mess)
                    self.send(Message(text=simi_text), thread_id=thread_id, thread_type=thread_type)
                elif '/timidol' in message_object.text:
                    self.idol_seach += 2
                    self.send(Message(text="Nhập tên đi bạn hiền"), thread_id=thread_id, thread_type=thread_type)
                elif self.idol_seach > 1 and message_object.text:
                    mess = message_object.text
                    idol = JavIdol().look_up_actress(mess)
                    counts = len(idol)
                    self.send(Message(text='Found {} babes named "{}"'.format(counts, mess)), thread_id=thread_id, thread_type=thread_type)
                    self.send(Message(text="{:<7} | {:17} | {}\t".format("ID", "Actress Name", "Japanese Name")), thread_id=thread_id, thread_type=thread_type)
                    for i in range(counts):
                        actress_id = idol[i]['id']
                        actress_name = idol[i]['name']
                        actress_japName = idol[i]['japanName']
                        self.send(Message(text="-Id idol: {:<7} \n-Tên idol: {:17} \n-Tên nhật: {}\t".format(actress_id, actress_name, actress_japName)), thread_id=thread_id, thread_type=thread_type)
                elif '/timmovies' in message_object.text:
                    self.movies_seach += 2
                    self.send(Message(text="Nhập ID idol đi tui tìm cho hihi"), thread_id=thread_id, thread_type=thread_type)
                elif self.movies_seach > 1 and message_object.text:
                    mess = message_object.text
                    movies = JavIdol().look_up_movies(mess)
                    counts = len(movies)
                    self.send(Message(text="Found {} videos for {}".format(counts, mess)), thread_id=thread_id, thread_type=thread_type)
                    for i in range(counts):
                        video_title = movies[i]['name']

                        if len(movies[i]['name']) > 50:
                            video_title = video_title.replace(video_title[49:], '...')
                        else:
                            video_title = movies[i]['name']

                        siteUrl = movies[i]['siteUrl']
                        video_code = siteUrl[(siteUrl.find("cid=") + 4):(len(siteUrl) - 1)].replace('00', '-', 1).upper()

                        message = "\n-Code: {:<15} \n-Tiêu đề: {}".format(video_code, video_title)
                        self.send(Message(text=message), thread_id=thread_id, thread_type=thread_type)
                else:
                    self.send(Message(
                        text='\n \n Tôi là Tú. \n- Tôi sẽ rep sau khi đi công việc về \n- Nếu muốn trò chuyện với simsimi gõ /simi. \n- Tìm idol gõ /timidol \n- Tìm phim gõ /timmovies \n- Tin nhắn của bạn: {0}'.format(
                            message_object.text)),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
saved_file_name = 'cookies.json'
with open(saved_file_name) as json_file:
    session_cookies = json.load(json_file)
client = AutoBot('camdauthienha99@gmail.com', 'demo100@', session_cookies=session_cookies)

session_cookies = client.getSession()
with open(saved_file_name, 'w') as f:
    json.dump(session_cookies, f, indent=4)
print(session_cookies)
client.listen()