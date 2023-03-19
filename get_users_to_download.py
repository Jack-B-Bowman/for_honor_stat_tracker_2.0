import json

def get_users_to_download(all_users_path = r"C:\Users\Jack Bowman\Documents\Programs\PytScripts\UserScraper\usersTesting03-15-1.txt",
                          failed_users_path = r"C:\Users\Jack Bowman\Documents\Programs\PytScripts\UserScraper\failedUsers.csv",
                          current_users_path = r"C:\Users\Jack Bowman\Documents\Programs\PytScripts\UbiScraper\player_ids.json"):
    all_users_file_path = all_users_path
    failed_users_file_path = failed_users_path
    current_users_file_path = current_users_path

    file = open(all_users_file_path,"r")
    all_users_file_data = file.readlines()
    file.close()

    all_users_dict = {}

    for line in all_users_file_data:
        split_line = line[:-1].split(",")
        username = split_line[1].replace("%20"," ")
        platform = split_line[0]
        player_string = f"{username}:{platform}"
        if player_string not in all_users_dict:
            all_users_dict[player_string] = 1
        else:
            all_users_dict[player_string] += 1

    file = open(failed_users_file_path,"r")
    failed_users_file_data = file.readlines()
    file.close()

    failed_users_dict = {}

    for line in failed_users_file_data:
        split_line = line[:-1].split(",")
        username = split_line[1]
        platform = split_line[0]
        player_string = f"{username}:{platform}"
        if player_string not in failed_users_dict:
            failed_users_dict[player_string] = 1
        else:
            failed_users_dict[player_string] += 1

    file = open(current_users_file_path,"r")
    current_users = json.load(file)
    file.close()

    users_to_get = []
    for player_string in all_users_dict:
        if player_string not in failed_users_dict and player_string not in current_users:
            users_to_get.append(player_string)  

    return users_to_get