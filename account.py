import time
import requests
# 
class Account:
    def __init__(self,email,key):
        self.email = email
        self.key = key
        self.ticket_birth_time = 0
        self.init_time = time.time()
        self.API_call_count = 0
        self.session = requests.Session()
        # the ticket is your API key for making calls to public-ubiservices.ubi.com
        self.ticket = ""
        # ubi's ticket expires three hours from creation. I've chosen two hours to be sage
        self.ticket_expire_seconds = 2 * 3600
        # default max is 500 calls an hour
        self.max_api_call_rate = 500 / 3600

    def login(self):
        url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Ubi-RequestedPlatformType": "uplay",
            "Ubi-AppId": "3587dcbb-7f81-457c-9781-0e3f29f6f56a",
            "GenomeId": "fd4135bb-409a-4e90-8587-a945f92e6c6d",
            "Authorization": f"Basic {self.key}",
            "Origin": "https://connect.ubisoft.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://connect.ubisoft.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Sec-GPC": "1",
            "TE": "trailers"
        }
        post_response = self.session.post(url=url,headers=headers).json()
        self.ticket = post_response["ticket"]
        self.ticket_birth_time = time.time()

    def execute_get_user_call(self,users,platform):
        self.API_call_count += 1
        usernames = ",".join(users)
        url = "https://public-ubiservices.ubi.com/v3/profiles"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Authorization": "ubi_v1 t=" + self.auth_string,
            "Ubi-AppId": "3587dcbb-7f81-457c-9781-0e3f29f6f56a",
            "Origin": "https://www.ubisoft.com",
            "DNT": "1",
            "Proxy-Authorization": "Basic MWJvd21hbmphY196YW1xZzp1d3RrYm1yZHEy",
            "Connection": "keep-alive",
            "Referer": "https://www.ubisoft.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Sec-GPC": "1",
            "TE": "trailers"
        }

        self.update_ticket()

        if self.get_API_call_rate() < self.max_api_call_rate:
            self.API_call_count += 1
            get_response = self.session.get(url=url, data="", headers=headers, params={"namesOnPlatform":usernames,"platformType":platform})
            return get_response
        
        raise("too many calls")

    # get the current API call rate of the account @per_unit is the unit of the rate e.g per hour, per minute, or per second
    def get_API_call_rate(self,per_unit):
        rate = self.API_call_count / (time.time() - self.init_time)
        if per_unit == "H":
            return rate * 3600
        if per_unit == "M":
            return rate * 60
        if per_unit == "S":
            return rate
        
        raise("per_unit must be 'H', 'M', or 'S'")
    
    # checks if the account's ticket is near expiring and relogs if so
    def update_ticket(self):
        call_time = time.time()
        if call_time - self.ticket_birth_time > self.ticket_expire_seconds:
            self.login()
            return True
        return False
        
