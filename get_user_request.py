class get_user_request:
    def __init__(self,username,platform,auth_string):
        self.username = username
        self.platform = platform
        self.params = {"namesOnPlatform":username,"platformType":platform}
        self.auth_string = auth_string
        self.data = ""
        self.url = "https://public-ubiservices.ubi.com/v3/profiles"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Ubi-SessionId": "47a3c4fb-0e45-4644-8e6f-3cbd72635140",
            "Authorization": "ubi_v1 t=" + auth_string,
            "expiration": "2023-03-19T20:41:12.076Z",
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
