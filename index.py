from fbchat import Client
from fbchat.models import *
import json

saved_file_name = 'cookies.json'
with open(saved_file_name) as json_file:
    session_cookies = json.load(json_file)
client = Client('camdauthienha99@gmail.com', 'demo100@', session_cookies=session_cookies)

session_cookies = client.getSession()
with open(saved_file_name, 'w') as f:
    json.dump(session_cookies, f, indent=4)
print(session_cookies)

if client.isLoggedIn():
    print("login true")
    client.listen()
    # thread_id = "100016561537741"
    # thread_type = ThreadType.USER
    # messages = client.fetchThreadMessages(thread_id=thread_id, limit=1)
    # # Since the message come in reversed order, reverse them
    # messages.reverse()
    #
    # # Prints the content of all the messages
    # for message in messages:
    #     print(message.text)
    #
    # thread = client.fetchThreadInfo(thread_id)[thread_id]
    # print("thread's name: {}".format(thread.name))
    # print("thread's type: {}".format(thread.type))
else:
    print("login fail")

