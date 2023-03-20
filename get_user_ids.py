import requests
import json
import time
from login_request import post_request
from get_user_request import get_user_request
from get_users_to_download import get_users_to_download


file = open("LoginInfo.json","r")
info = json.load(file)
file.close()

keys = []
for user in info:
     keys.append(info[user]["key"])

s = requests.Session()
auth_strings = []
# log in using post to get auth_string
login_data = post_request(keys[0])
post_response = s.post(url=login_data.url,data=login_data.payload,headers=login_data.headers).json()
auth_strings.append(post_response["ticket"])




# search up a user
def get_user(session, get_data):
        get_response = session.get(url=get_data.url, data=get_data.data, headers=get_data.headers, params=get_data.params)
        return get_response

# re-submit post to get new auth_string
def relog(session,login_data):
        post_response = session.post(url=login_data.url,data=login_data.payload,headers=login_data.headers).json()
        auth_string = post_response["ticket"]
        return auth_string

users_to_download = get_users_to_download()

player_ids = {}
count = 0
start_time = time.time()
swap_count = 0
auth_string = auth_strings[swap_count]
print()
for user_string in users_to_download:

    player = user_string.split(":")
    username = player[0]
    platform = player[1]
    get_data = get_user_request(username,platform,auth_string)
    get_response = get_user(s,get_data)
    time.sleep(4)
    if get_response.status_code == 429:
        swap_count += 1
        login_data = post_request(keys[swap_count % len(auth_strings)])
        auth_string = relog(s,login_data)
        get_response = get_user(s,get_user_request(username,platform,auth_string))

    if get_response.status_code == 401:
        login_data = post_request(keys[swap_count % len(auth_strings)])
        auth_string = relog(s,login_data)
        get_response = get_user(s,get_user_request(username,platform,auth_string))

    try:
        print(f"\r                                              ",end="")
        text = get_response.json()["profiles"][0]["nameOnPlatform"]
        print(f"\r{text}",end="")
    
    except:
         ...
    if get_response.status_code != 200:
        print(f"get_response.status_code : {get_response.status_code}")
        print(get_response.json())
        input()
    else:
        player_ids[user_string] = get_response.json()
    count +=1

    if count % 100 == 0:

        swap_count += 1
        login_data = post_request(keys[swap_count % len(keys)])
        print(keys[swap_count % len(keys)])
        file = open(rf".\player_id_files\player_id_{count}.json","w")
        json.dump(player_ids,file,indent=4)
        file.close()
        player_ids = {}
        print(f"time for last 100 = {(time.time() - start_time):.2f}")
        start_time = time.time()

file = open(rf".\player_id_files\player_id_{count}.json","w")
json.dump(player_ids,file,indent=4)
file.close()
player_ids = {}


