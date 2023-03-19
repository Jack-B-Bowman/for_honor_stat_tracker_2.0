import json
import os

def mergeJSON(dir=r"player_id_files",originalFilePath=r".\player_ids.json"):
    directory = dir
    mergedData = ""
    if originalFilePath != "":
        originalFile = open(originalFilePath,"r")
        mergedData = json.load(originalFile)
    else:
        mergedData = {}

    count = 0
    for filename in os.listdir(directory):

        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and f[-4:] == 'json':
            file = open(f,"r")
            try:
                newData = json.load(file)
            except Exception as e:
                print(e)
                print(filename)
            for user in newData:
                count += 1

                if(count % 1000 == 0):
                    print(f"\r{count}",end="")
                
                mergedData[user] = newData[user]
            file.close()
    return mergedData

mergedData = mergeJSON()
file = open(r".\player_ids.json","w")
json.dump(mergedData,file,indent=4)
file.close()