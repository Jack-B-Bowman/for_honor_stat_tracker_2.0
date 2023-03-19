import requests
import json
import time
from login_request import post_request
from get_user_request import get_user_request
from get_users_to_download import get_users_to_download

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.text)

s = requests.Session()

login_data = post_request()
# post_responce = s.post(url=login_data.url,data=login_data.payload,headers=login_data.headers).json()
auth_string = 'ewogICJ2ZXIiOiAiMSIsCiAgImFpZCI6ICIzNTg3ZGNiYi03ZjgxLTQ1N2MtOTc4MS0wZTNmMjlmNmY1NmEiLAogICJlbnYiOiAiUHJvZCIsCiAgInNpZCI6ICI5ZjgzOTI3Ny1iOWM5LTRkYWEtOGU0YS1lODRiNTg2ZDgzOWEiLAogICJ0eXAiOiAiSldFIiwKICAiZW5jIjogIkExMjhDQkMiLAogICJpdiI6ICJUNHdiRi1kM2JfSGNPY2ZESkhnWWRRIiwKICAiaW50IjogIkhTMjU2IiwKICAia2lkIjogImJhMGMyNjJkLTVjY2QtNGE3My05YjBlLWIwNDA1YjU2YmQxNCIKfQ.cokTL9JRXqYZU37M0p3nqQwoNtW2u_nlSXLpQxWvqB0mK4wIt9DLXAlN_GkzKYUiOL0McFQXOpij_bwoJRp9YqUago8OhkfAHeAlUzYDGrnqd-F_rTcStYLZywDTIKm4lRljFrl8t3lb242ysYe2e_vSi7bEKYPItKNZOdGufmRd5G3iRuuTZQZIdWiLa56T80-7MJE-3GD3PJE6NX25KJWvKehs9b89JA-QkPaxnI-Ulp748RdljE0QVukBNHJ0JeAfOqYc7kt1-OMZRYy4NNfKqXV59tYpdl-mDxu7PWogaert4YxA_vn7O9foARoZ8YgzRrMNb3mHtt16qjmn8jbRpJl6-g4X-EvA1HKX44RTe0yM_B10Qi_2OaDTtYHisMeO4ggg1TyBOGgumrF-6XYB06HAHtD-3y0iw_jde-amu2BFrqnzUcLJPCmDN3lVT-54WFnJh59LudiE8UpiAnsmYZ2Qh1fB5BhAkmB6RcmU13hJ15qh3DEKptuK5cPgzY-p662NFapgzmmQrGz_izfgLaWAn0qLsY38AGeIUq4QZQOnOOsbSMu_9v5s0VzoPpF8gY-Oy9X03IfLZD8aROCF_Rr1n4rPEy6cpyn3ANMcJuCXvGI7hrQ1QCQ-eETxQjJ4mY0mZGa2HWad5LsMUZ5EFsyovIIz21XrG7AVxMpAGaayMrixmPln5SRFFlVR449BhDFXtt_zFFSAYLEfdlO_yB0bxNvJPbJZRLSjoDKf765HL66G6cohcuh8Q52j0l2DbszJ3z7xc8rQx9C91DwYYKW9WHcVziZpv7aVW-bme7vwd8nJaBDEcrfc72_Pp46DP2s0FemsmeR_dQ6-A3uIfeNXvMxg_0gwJ_r2sT2TLLF--mqDsVQqGvahoU8_RTfr7RZ7iC3jKJ-pKYTkuh4yKyorZfq9P4vnOIdYvOW1h9CFCCotKTBwO2MHg-QXn1VjpyO8C0FdnxWDPCnerE2wUC6MwxV6jTuClS_SX0ywPzegLoX-QF13efaC37uC6NNygEK8C_SxwWcaXQ8kLwJmzIage0qC-brXkg5OMip_xShMRQ5HLEcuEkJ8Z9u0UOF9fLqtkpb0wTYAcWw6ZYmagDIV1FyFvs2ygxTlcIZsn-nv5F2WAV03LtIT6-D9Zrd_rdJrufjNf33qoMuIetrd-8Bb7CKtq9hBC6GBQRX52pUu8W3t5yBL2HwlGboxi2YGOjgUypZMZOmqyw2ZkcWXUmZE--UCJ94BM-1OjsiYbIUo8k2cbFp7q4iq4NFQQE7bxImhkrL15TFNgjYSg5Xx_7_O4T_g6SxNWhcHqFdnXanJTZ5cBof9hC9D9SImPTDeLxRASaqT21pxBSy6UaoMFQtGPKiOFEUSTcp0417VIBc5-vvVVbsJFCASVnCTH7kAWKNHmmiPWL8SPFnaZVNvAkzEwIykI3E7sr-xAVT8riE6buQEJ7w3LydgAVMxLnsd4N4o-5NzxhwQKaY1xzz5dahfpNngVEEykYBDBVWEDD90Uhyc0u4pJ6xF2KjFP7HenuwdHG7P7jKKg5LZ5FggHjrWTGh6uhXuMiFacp1gWy6WBo-2_055gtA8BratjfepsAgSbxhE_kRd2XqgPuSJAuz4JFDwIxDCeMxLs2QbZNblEUlJ16Sn2CodOucH6l87wZsi5JuA11U5GwxMVZbR7bVsaFLDrUTw2BzAJbWHxmtZvfR9IGwG1yQzr4_hUUloAbrOWGUk6sDVc4nssYygn_Jv_7C3iDmpB4kZBUQBik2igawdsNdBbsmgqkVGEXjb7iNRWGiQS8tKj4dZtoRcVhB0fcmX7XyB3rClFEqhZjasLE0YCMaATCym1QIkv_gb5YqUgt0qYycIDsod4n7ErKdlPmDYvtUWrpDiEPg.NaDSKvW_pK_Ir0lU6ogt6gyURGDTlqITJDR1677MBm0'
get_data = get_user_request("aaalvariyooo","psn",auth_string)

get_response = s.get(url=get_data.url, data=get_data.data, headers=get_data.headers, params=get_data.params)
if get_response.status_code != 200:
    print("break")

users_to_download = get_users_to_download()

player_ids = {}
count = 0
start_time = time.time()
for user_string in users_to_download:

    player = user_string.split(":")
    username = player[0]
    platform = player[1]
    get_data = get_user_request(username,platform,auth_string)
    get_response = s.get(url=get_data.url, data=get_data.data, headers=get_data.headers, params=get_data.params)
    if get_response.status_code != 200:
        print("break")
    else:
        player_ids[user_string] = get_response.json()
    count +=1

    if count % 100 == 0:
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


