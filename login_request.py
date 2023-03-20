class post_request:
    def __init__(self,key,url="https://public-ubiservices.ubi.com/v3/profiles/sessions",
                 query_string={},
                payload="{rememberMe:true}"):
        self.url = url
        self.query_string = query_string
        self.payload = payload
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Ubi-RequestedPlatformType": "uplay",
            "Ubi-AppId": "3587dcbb-7f81-457c-9781-0e3f29f6f56a",
            "GenomeId": "fd4135bb-409a-4e90-8587-a945f92e6c6d",
            "Authorization": f"Basic {key}",
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
