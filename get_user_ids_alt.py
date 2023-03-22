import json
import time
import account
from get_users_to_download import get_users_to_download

CHUNK_SIZE = 2

file = open("LoginInfo.json","r")
info = json.load(file)
file.close()

accounts = []
for acc in info:
    accounts.append(account.Account(acc["email"],acc["key"]))

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

users_to_download = get_users_to_download()

player_ids = {}
count = 0
start_time = time.time()
print()
for platform in users_to_download:
    for usernames in chunker(users_to_download[platform],CHUNK_SIZE):
        account_index = count % len(accounts)
        acc = accounts[account_index]
        data = get_response.json()["profiles"]
        for player in data:
            player_string = player["nameOnPlatform"] + ":" + player["platformType"]
            player_ids[player_string] = player


